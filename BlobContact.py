##Simple azurwe storage blob comm
##Storage container static URL: https://storagebackupstuff.blob.core.windows.net/storagecontainer
##Anonymous Access: No
##Access Method: SAS Token + URI
##Note: Ensure you install .\virt\Scripts\pip.exe install azure-storage-blob azure-identity, from the respective virt env


##Object Model of Blob Storage Access:
##Source: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli&pivots=blob-storage-quickstart-scratch

## Azure Blob Storage is optimized for storing massive amounts of unstructured data. 
## Unstructured data is data that doesn't adhere to a particular data model or definition, such as text or binary data. 
## Blob storage offers three types of resources:
#The storage account
#A container in the storage account
#A blob in the container


##We are Accessing the storage account with our dedicated SAS Token
##Next, we access to Container, via ContainerClient
##Finally, we access, add, delete, and manipulate files at will within our blob with BlobClient!





import os, uuid, sys
from dotenv import load_dotenv

 ##TO DO:
        ##### - ADD ARGPARSE FOR DELETE / UPLOAD FUNCTION

        ##### - ADD DELETE FUNCTION
        
        ###SEPERATE PYTHON FUNCTIONALITY FOR GUI OF FOLDER EXPLORER TO "Upload" a folder or file
        
UPLOADIR = "/Upload"

def AzureImports(cname, sass):

    #The BlobServiceClient class allows you to manipulate Azure Storage resources and blob containers.
    #The ContainerClient class allows you to manipulate Azure Storage containers and their blobs.
    #The BlobClient class allows you to manipulate Azure Storage blobs.
    try:
        from azure.identity import DefaultAzureCredential
        from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
        from azure.core.exceptions import HttpResponseError, ServiceRequestError, ResourceExistsError, ResourceNotFoundError


        #In Future, use envs to access this 
        account_url = os.getenv("ACCTURL")
        print(repr(cname), account_url)
        ##default_credential = DefaultAzureCredential()



        ##After testing to ensure uri exists?

        try:
            load_dotenv()
            import requests
            from requests.exceptions import ConnectionError, Timeout, RequestException

            if not account_url.startswith("https://"):
                print("Warning... URi is not being access with secure HTTPS method...")
            try:
                resp = requests.head(account_url, timeout=5)

                if resp.status_code != 404:
                    print("Server Is Active and or Existent")
                    #Grab Client for BLOB
                    blob_service_client = BlobServiceClient(account_url=account_url, credential=sass)
                    #Grab Client for CONTAINER WITHIN BLOB
                    container_client = blob_service_client.get_container_client(cname)
                    info = blob_service_client.get_account_information()
                    #containerInfo = container_client.get_container_properties("str")
                    #print(containerInfo)
                    acctInfo = blob_service_client.list_containers()
                    print(list(acctInfo))
                    if info:
                        print("\n\n\n Connected To Azure Blob Storage!")
                        print("Request ID: %s "% (info["request_id"]))
                        print("Version: %s "% (info["version"]))
                        print("Account Type: %s"%(info["account_kind"]))




                    #List 'Blobs' in container (Requires LIST perm in SAS token)
                    BlobContainerInfo = (blob_service_client.list_containers())
                    for x in BlobContainerInfo:
                        if x.name == cname:
                            print("\n\n\n")
                            print("Selected Container Name: %s"% (x.name))
                            print("Selected Container State: %s, %s "% (x.lease['status'], x.lease['state']))
                            if x.public_access == None:
                                print("Anonymous Access Disabled!")
                                
                        
                    





                else:
                    print("Blob Storage Server Does not Exist! Check URI again....")
                    sys.exit()
            
            except HttpResponseError as hRE:

                ##TODO: Attempt to generate a new Auth SAS token for the user automatically, but temporarily
                print("\n\n SAS Auth Potentially Failed... Check Token Validity")
                print("\n\n Attempted Resource to be accessed: %s, \n\n Attempted URI Used \n\n: %s"% (cname, account_url))
                sys.exit()
            
            except TimeoutError as tE:
                sys.exit(f"The Requested Server {account_url} has timed out.... Is Blob Storage Accessible?")
            
            except ServiceRequestError as sRE:
                sys.exit(f"Connectivity Issues: {sRE}")




        except ImportError as iEE:
            sys.exit(f"{iEE}")

        return blob_service_client




    except ImportError as iE:
        sys.exit(f"Modules failed to import // Not Installed: azure-storage-blob azure-identity \n\n {iE}")



def getFileSize(filepath):
    #Returns size of file in BYTES
    return os.path.getsize(filepath)

def Upload(blob_service_client, local_file_name, container_name):

    ##Check if upload dir exist
    curDir = os.getcwd()
    workDir = curDir + UPLOADIR
    rFile = os.path.join(workDir, local_file_name)
    choice = None
    ovWrite = False


    if os.path.exists(workDir):
        print("Correct Working Directory set and exists...  %s"% (workDir))
        print("All Current Files that can be copied over to blob storage: %s"% (os.listdir(workDir)))
        choice = input("Upload Entire Directory of files %s, or just singular file %s (f/d): "% (workDir, rFile))
        if choice == "d":
            local_file_name = os.getenv("DIR2UPLOAD")


    else:
        #In future just make dir with os.mkdir and then get copied files tht way
        sys.exit("Cannot Find usual Working Directory...")

    #Set container client
    container_client = blob_service_client.get_container_client(container_name)
    #Current 'Blobs' Or Files Already Shared and check if file we are uploading exists
    bList = container_client.list_blobs()
    if bList != ' ' or None:
        for b in bList:
            if str(b.name) == local_file_name:
                print("NOTICE: File or Directory Blob Appears To Already Exist In Cloud!")

    print("\nUploading to Azure Storage as blob: %s"% (local_file_name))

    ##Attempt to read bytes, and upload file / Dir
    try:
        if choice == "f":
            with open(rFile, mode="rb") as data:
                # Create a blob client using the local file name as the name for the blob
                blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
                #Upload read bytes, do not overwrite data if pre-existing
                blob_client.upload_blob(data, overwrite=False)
                #blob_client.download_blob(data)
        elif choice == "d":
            for root, dirs, files in os.walk(workDir):
                for fileName in files:
                    print(getFileSize(os.path.join(root, fileName)))
                    print(f"Uploading {fileName}")
                    lFilePath = os.path.join(root, fileName)
                    blob_client = blob_service_client.get_blob_client(container=container_name, blob=fileName)
                    with open(lFilePath, mode='rb') as dirToUpload:
                        blob_client.upload_blob(dirToUpload, overwrite=True)

        

    



    except PermissionError as pE:
        sys.exit(f"Permission Error on file {local_file_name}")

    except Exception as eE:
        sys.exit(f"{eE}")
    

    


def main():
    load_dotenv()
    sass = os.getenv("SAS")
    cname = os.getenv("CNAME")
    local_file_name = os.getenv("FILE2UPLOAD")
    preReq = AzureImports(cname, sass)
    #print(sass)
    if preReq:
        ##TO DO:
        ##### - ADD ARGPARSE FOR DELETE / UPLOAD FUNCTION

        ##### - ADD DELETE FUNCTION
        Upload(preReq, local_file_name=local_file_name, container_name=cname)




if __name__ == "__main__":
    main()
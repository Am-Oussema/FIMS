import os
import time
import hashlib

def compute_hash(file_path):
    sha256=hashlib.sha256()
    try:
        with open(file_path,'rb') as f:
            while True:
                chunk=f.read(8192)
                # print("chunk",chunk)
                if not chunk:
                    break
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return None
# print(compute_hash("C:\ComboKey\manual.pdf"))
def scan_folder(root_path):
    results={}
    for root,dirs,files in os.walk(root_path):
        # print(root,dirs,files)
        for file in files:
            abs_path= os.path.join(root,file)
            # relative path makes snapshots portable
            rel_path=os.path.relpath(abs_path,root_path)
            file_hash=compute_hash(abs_path)
            try:
                stats=os.stat(abs_path)
                results[rel_path] = { "hash": file_hash, "size": stats.st_size,"mtime": int(stats.st_mtime)} #save hash,size,modif time

            except Exception:
                # Some files (permissions, broken links) might fail; still record hash
                results[rel_path]={ "hash": file_hash , "size":None , "mtime":None }

    return results

# print(scan_folder("C:\FIFA 23 Live Editor\data"))
# Week-06/Task06.py
# Task 6: Create a program to use Python's asyncio library to
# perform asynchronous I/O operations.
print ("=== TASK #6 OUTPUT ===")

import time        
import asyncio       
def download_file(file_name):
    print(f"Starting download: {file_name}")
    time.sleep(3)   
    print(f"Finished download: {file_name}")

def sync_main():
    start = time.time()                
    download_file("file1.pdf")         
    download_file("file2.pdf")         
    end = time.time()
    print(f"Synchronous total time: {end - start:.2f} seconds")

async def async_download(file_name):
    print(f"Starting download: {file_name}")
    await asyncio.sleep(3) 
    print(f"Finished download: {file_name}")
    
async def async_main():
    start = time.time()
    t1 = asyncio.create_task(async_download("file1.pdf"))
    t2 = asyncio.create_task(async_download("file2.pdf"))
    await t1
    await t2
    end = time.time()
    print(f"Asynchronous total time: {end - start:.2f} seconds")

sync_main()       
asyncio.run(async_main())  

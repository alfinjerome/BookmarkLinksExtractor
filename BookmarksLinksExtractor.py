import re

def extract_urls(bookmark_file_path, output_file_path=None):

    unique_urls = set() 
    
    url_regex = re.compile(r'href\s*=\s*["\'](.*?)["\']', re.IGNORECASE)

    try:
        with open(bookmark_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{bookmark_file_path}'")
        return
    except Exception as e:
        print(f"Error reading file '{bookmark_file_path}': {e}")
        return

    extracted_urls = url_regex.findall(html_content)

    for url in extracted_urls:
        unique_urls.add(url) 

    final_urls = sorted(list(unique_urls))

    if final_urls:
        print(f"\nFound {len(final_urls)} unique URLs:")
        if output_file_path:
            try:
                with open(output_file_path, 'w', encoding='utf-8') as outfile:
                    for url in final_urls:
                        outfile.write(url + "\n")
                print(f"URLs saved to '{output_file_path}'")
            except Exception as e:
                print(f"Error writing to output file '{output_file_path}': {e}")
        else:
            for url in final_urls:
                print(url)
    else:
        print("No URLs found.")

if __name__ == "__main__":

    bookmarks_file = input("Enter the bookmark file path: ").strip()
    output_txt_file = input("Enter the output file path (leave blank to print to console): ").strip()

    if not bookmarks_file:
        print("Error: The bookmark file path cannot be empty.")
    
    if not output_txt_file:
        output_file_path= None    

    
    extract_urls(bookmarks_file, output_txt_file)

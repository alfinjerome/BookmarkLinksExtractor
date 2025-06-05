import re

def extract_urls(bookmark_file, output_file=None):

    unique_urls = set() 
    
    url_regex = re.compile(r'href\s*=\s*["\'](.*?)["\']', re.IGNORECASE)

    try:
        with open(bookmark_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{bookmark_file}'")
        return
    except Exception as e:
        print(f"Error reading file '{bookmark_file}': {e}")
        return

    extracted_urls = url_regex.findall(html_content)

    for url in extracted_urls:
        unique_urls.add(url) 

    final_urls = sorted(list(unique_urls))

    if final_urls:
        print(f"\nFound {len(final_urls)} unique URLs:")
        if output_file:
            try:
                with open(output_file, 'w', encoding='utf-8') as outfile:
                    for url in final_urls:
                        outfile.write(url + "\n")
                print(f"URLs saved to '{output_file}'")
            except Exception as e:
                print(f"Error writing to output file '{output_file}': {e}")
        else:
            for url in final_urls:
                print(url)
    else:
        print("No URLs found.")

if __name__ == "__main__":

    bookmark_file = input("Enter the bookmark file path: ").strip()
    output_file_path = input("Enter the output file path (leave blank to print to console): ").strip()

    if not bookmark_file:
        print("Error: The bookmark file path cannot be empty.")
    else:
        output_file = None
        if output_file_path:
            output_file = output_file_path

    
        extract_urls(bookmark_file, output_file)

import sys
import hashlib

def main():
    try:
        text = sys.argv[1]
        save_file = sys.argv[2]
        if os.path.exists(save_file):
            print("File location found.")
        else:
            print("File location not found.")
            main()
    except IndexError:
        usage = print("Usage : python [python file location] [text to be encrypted] [save file location]")
        return usage
        print("\n")
        main()
    except PermissionError:
        print("Please write a file with access permission.")
        main()
    except RecursionError:
        usage = print("Usage : python [python file location] [text to be encrypted] [save file location]")
        return usage
        print("\n")
        main()

    def encryption():
        print("Encrypting...")
        encrypted = hashlib.md5(text.encode()).hexdigest()
        print(f"Unencrypted : {text}, encrypted : {encrypted}")
        write_on_file = f"{encrypted}:{text}"
        print(write_on_file)
        def write_on_file_func():
            with open(save_file, "a", encoding="utf-8") as file:
                file.write("\n"+write_on_file)
                print("Writed on file the encrypted text and uncrypted text.")
        write_on_file_func()
    encryption()

main()

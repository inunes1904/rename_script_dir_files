import os
import unicodedata

def removeAccents(text):
        text = str(text)
        normalized = unicodedata.normalize("NFKD", text)
        normalized = "".join([c for c in normalized if not unicodedata.combining(c)])
        normalized = normalized.replace("'", "")
        normalized = normalized.replace("ç", "c")
        return normalized
        
def main():
    
    path = "/Path/You/Want"

    for roots, dirs, files in os.walk(path):   
        for file in files:
            try:
                valueFiles = removeAccents(file)
                os.rename(os.path.join(roots, file), os.path.join(roots, valueFiles)) 
            except:
                print('Ingored')

    counter = 0
    for roots, dirs, files in os.walk(path):     
        counter += 1
    n = 0
    while n != counter:
        for roots, dirs, files in os.walk(path):     
            test = len(dirs)        
            for dir in dirs:
                if test == 1:
                    try:
                        old_path = path + '/' + dir
                        new_path = removeAccents(old_path)
                        os.rename(old_path, new_path)
                        path = new_path
                    except:
                        print('Ingored')
                else:  
                    try:                    
                        old_path = path + '/' + dir
                        print(old_path)
                        new_path = removeAccents(old_path)
                        print(new_path)
                        os.rename(old_path, new_path)
                    except:
                        print('Ignored')
        n += 1
                

if __name__ == '__main__':
    main()
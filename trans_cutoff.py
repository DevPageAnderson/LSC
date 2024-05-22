import os
import random

# 지정된 디렉토리 경로
directory = r'C:\Users\Public\Documents\Photon Kinetics\PKSL\Archived Data'
output_file = r'\\156.147.230.100\c\lg\data'

# 디렉토리 내의 첫 번째 CSV 파일을 찾습니다
csv_file = next((f for f in os.listdir(directory) if f.endswith('.csv')), None)

if csv_file:
    file_path = os.path.join(directory, csv_file)
    
    # CSV 파일을 읽습니다
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 필요한 값을 저장할 변수 초기화
    id_value = None
    cutoff_value = None
    
    # 각 줄을 순회하며 필요한 값을 찾습니다
    for i, line in enumerate(lines):
        #if 'Fiber ID' in line and i + 1 < len(lines):
        if 'Fiber ID' in line and i < len(lines):
            id_value = lines[i].strip().split(",")[1]

        elif 'Cut-off Wavelength (nm)' in line and i < len(lines):
            try:
                #cutoff_value = int(float(lines[i + 1].strip().split()[0]))
                cutoff_value = (lines[i].strip().split(",")[1])
                cutoff_value = int(float(cutoff_value))
                
            except ValueError:
                print("Error: Cut-off Wavelength value is not a valid number.")
                cutoff_value = None
    
    # 결과 출력
    if id_value is not None and cutoff_value is not None:
        #print(f'id: {id_value}')
        #print(f'cutoff: {cutoff_value}')
        numbers = list(range(1, 100))

        random_number = random.choice(numbers)

        random_string = f'{random_number:02}'

        
        file_name = "T" + random_string + ".dat"
        output_file = os.path.join(output_file, file_name)

        # 파일에 문자열을 씁니다
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f'T {id_value} {cutoff_value}')
    else:
        print('Required data not found in the file.')
else:
    print('No CSV files found in the directory.')


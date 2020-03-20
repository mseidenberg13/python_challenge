import os
import csv

candidates = []
votes = 0
vote_count = []
data = ['1']

for files in data:
    PyPoll_csv = os.path.join("Resources","election_data.csv")
      
    with open(PyPoll_csv) as csvfile:
       csvreader = csv.reader(csvfile, delimiter=',')
       line = next(csvreader,None)

       for line in csvreader:        
            votes = votes + 1
            candidate = line[2]
          
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_count[candidate_index] = vote_count[candidate_index] + 1
            else:
                candidates.append(candidate)
                vote_count.append(1)
               
    percentages = []
    max_votes = vote_count[0]
    index = 0
    
    for count in range(len(candidates)):
        vote_percentage = vote_count[count]/votes*100
        percentages.append(vote_percentage)
        if vote_count[count] > max_votes:
            max_votes = vote_count[count]
            print(max_votes)
            index = count
    winner = candidates[index]
   
    percentages = [round(i,2) for i in percentages]
    
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {votes}")
    print("--------------------------")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
    print("--------------------------")
    print(f"Winner:  {winner}")
    print("--------------------------")

    output_file = PyPoll_csv[0:-4]
    write_PyPoll_csv = f"{output_file}PyPoll_results.txt"
    filewriter = open(write_PyPoll_csv, mode = 'w')
    
    filewriter.write("Election Results\n")
    filewriter.write("-----------------------------\n")
    filewriter.write(f"Total Votes:  {votes}\n")
    filewriter.write("-----------------------------\n")
    for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})\n")
    filewriter.write("-----------------------------\n")
    filewriter.write(f"Winner:  {winner}\n")
    filewriter.write("-----------------------------\n")
    
    filewriter.close()
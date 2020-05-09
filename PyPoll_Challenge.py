# Import  dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes=0

#Initialize a list of candidates
candidate_options=[]

#Initialize a dictionary of candiates vote.
candidate_votes={}

#Initialize a variable empty string for winning candidate.
winning_candidate=""
#Set winning count to zero
winning_count=0
#Set winning percentage to zero
winning_percentage=0

#Initialize a list of counties.
county_options=[]
#Initialize a dictionary of county votes.
county_votes={}
#Initialize a an empty string variable for county with the largest turnout.
largest_county_turnout=""
#Set largest turnout to zero
turnout_count=0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Skip the header row.
    headers = next(file_reader)
  
    # Print each row in the CSV file.
    for row in file_reader: 
        #incremment the vote counter by 1.
        total_votes=total_votes + 1

        #print candidates name from each row.
        candidate_name=row[2]
        #print county name for each row.
        county_name=row[1]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #then add him to the list of candidates.
            candidate_options.append(candidate_name)

            #start tracking candidate vote.
            candidate_votes[candidate_name]= 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # if the county does not match any existing counties...
        if county_name not in county_options:
            #then add it to the list of counties.
            county_options.append(county_name)

            #start tracking county votes.
            county_votes[county_name]= 0

        # Add a vote to that counties's count.
        county_votes[county_name]+=1

#save the results to our text file.
with open (file_to_save,'w') as txt_file:
    #print the final vote count to the terminal.
    election_results=(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes :{total_votes:,}\n"
        f"-------------------------\n"
        f"                         \n"
        f"County Votes:             \n")
    print(election_results, end="")
    #save the final vote count to the text file.
    txt_file.write(election_results)

    #Determin the percentage of each county votes by looping through the counts.
    #Iterate through county list.
    for county_name in county_options:
        #retrieve vote count for each county.
        countyvotes=county_votes[county_name]
        #calculate the percentage of votes
        county_votes_percentage=float(countyvotes)/float(total_votes)*100
        county_results=(
            f"{county_name}: {county_votes_percentage:.1f}% ({countyvotes:,})\n")
        #print each counties name, vote count and percentage votes.
        print(county_results)
        #Save the counties results to our text file
        txt_file.write(county_results)

        #Determine Largest County Turnout.
        if(countyvotes>turnout_count) :
            turnout_count=countyvotes
            largest_county_turnout=county_name

    #print largest  county turnout result to the terminal.
    turnout_count_result=(
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n")
    print(turnout_count_result)
    #save largest county turnout on text file.
    txt_file.write(turnout_count_result) 

    #Determin the percentage of each candidates votes by looping through the counts.
    #Iterate through candidate list.
    for candidate_name in candidate_votes:
        #retrieve vote count for each candidate.
        votes=candidate_votes[candidate_name]
        #calculate the percentage of votes
        votes_percentage=float(votes)/float(total_votes)*100
        candidate_results = (
            f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
        #print each candidates name, vote count and percentage votes.
        print(candidate_results)
        #Save the candidates results to our text file
        txt_file.write(candidate_results)
        #Determine winning vote count, winning percentage and candidate.
        if(votes>winning_count) and(votes_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=votes_percentage
            winning_candidate=candidate_name

    #print winning candidates' results to the terminal.
    winning_candidate_summary= (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count:{winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")

    print(winning_candidate_summary)
    #save the wininng candidates summary to the text file.
    txt_file.write(winning_candidate_summary)
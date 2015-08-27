import requests
import json

def get_sm_survey_respondent_ids(surveyid):
	respondent_ids=[]
	client = requests.session()
	client.headers = {
		"Authorization": "bearer %s" % 'paTBz61kMlD0mPWrsaHR3921EuYbHlBvqU0GDZQ.5nahBvB1GbdZpbh2WnOzXY4SJpMkHXENcoejRFTmPgdAVNY681GkIsJgilCmaeSARQ0=',
		"Content-Type": "application/json"
		}
	client.params = {
		"api_key": "d7fk9g6bmcf6rw3jrzhqpn3r"
		}
	
	HOST = "https://api.surveymonkey.net"
	SURVEY_LIST_ENDPOINT = "/v2/surveys/get_respondent_list"

	uri = "%s%s" % (HOST, SURVEY_LIST_ENDPOINT)

	data = {"survey_id": "68255536"}
	response = client.post(uri, data=json.dumps(data))
	response_json = response.json()
	#survey_list = response_json["data"]
	for i in range(len(response_json["data"]["respondents"])):
		respondent_ids.append( response_json["data"]["respondents"][i]["respondent_id"])	
	
	return respondent_ids
	
def get_sm_survey_response(surveyid):
	client = requests.session()
	client.headers = {
		"Authorization": "bearer %s" % 'paTBz61kMlD0mPWrsaHR3921EuYbHlBvqU0GDZQ.5nahBvB1GbdZpbh2WnOzXY4SJpMkHXENcoejRFTmPgdAVNY681GkIsJgilCmaeSARQ0=',
		"Content-Type": "application/json"
		}
	client.params = {
		"api_key": "d7fk9g6bmcf6rw3jrzhqpn3r"
		}
	
	HOST = "https://api.surveymonkey.net"
	SURVEY_LIST_ENDPOINT = "/v2/surveys/get_survey_details"

	uri = "%s%s" % (HOST, SURVEY_LIST_ENDPOINT)
	sm_survey_output = {}
	sm_survey_metadata = {}
	data = {"survey_id": "68255536"}
	response = client.post(uri, data=json.dumps(data))
	response_json = response.json()
	#print response_json["data"]["pages"][0]["questions"]
	for i in range (len(response_json["data"]["pages"][0]["questions"])):
		a = response_json["data"]["pages"][0]["questions"][i]["question_id"]
		b = response_json["data"]["pages"][0]["questions"][i]["heading"]
		sm_survey_metadata[a] = b
		for j in range ( len ( response_json["data"]["pages"][0]["questions"][i]["answers"])):
			x= response_json["data"]["pages"][0]["questions"][i]["answers"][j]["answer_id"]
			y = response_json["data"]["pages"][0]["questions"][i]["answers"][j]["text"]
			sm_survey_metadata[x]=y
	#print sm_survey_metadata
	#print response_json["data"]["pages"][0]["questions"][1]["heading"]
	#print response_json["data"]["pages"][0]["questions"][1]["answers"][1]["text"]
	#print response_json["data"]["pages"][0]["questions"][1]["answers"][1]["answer_id"]

	SURVEY_LIST_ENDPOINT = "/v2/surveys/get_responses"

	uri = "%s%s" % (HOST, SURVEY_LIST_ENDPOINT)

	respondent_ids = get_sm_survey_respondent_ids (68255536) 
	print respondent_ids
	data = {"survey_id": "68255536" , "respondent_ids" : respondent_ids}
	response = client.post(uri, data=json.dumps(data))
	output = response.json()

	#survey_list = response_json["data"]
	response_output=[]
        for i in range(len(output["data"])):
           	#print i
           	Que1 = output["data"][i]["questions"][0]["question_id"]
           	Ans1 = output["data"][i]["questions"][0]["answers"][0]["text"]
           	Que2 = output["data"][i]["questions"][1]["question_id"]
           	Ans2 = output["data"][i]["questions"][1]["answers"][0]["row"]
           	Que3 = output["data"][i]["questions"][2]["question_id"]
           	Ans3 = output["data"][i]["questions"][2]["answers"][0]["row"]
           	Que4 = output["data"][i]["questions"][5]["question_id"]
           	Ans4 = output["data"][i]["questions"][5]["answers"][0]["text"]
            
           	sm_survey_output["Q1"] = sm_survey_metadata[Que1]
           	sm_survey_output["A1"] = Ans1 
           	sm_survey_output["Q2"] = sm_survey_metadata[Que2] 
           	sm_survey_output["A2"] = sm_survey_metadata[Ans2]
           	sm_survey_output["Q3"] = sm_survey_metadata[Que3]
           	sm_survey_output["A3"] = sm_survey_metadata[Ans3]
           	sm_survey_output["Q4"] = sm_survey_metadata[Que4]
           	sm_survey_output["A4"] = Ans4
           	
           	response_output.append(sm_survey_output.copy())
    		print response_output       	
	return response_output

#print get_sm_survey_response(123)
#print get_sm_survey_respondent_ids(123)
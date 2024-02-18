import json
from flask import jsonify, request
from .utils import data
from .utils import *


def configure_routes(app):

    @app.route('/')
    def index():
        return "Welcome to the DALI MEMBER API!"

    # Get members
    @app.route('/members', methods=['GET'])
    def get_members():
    
        return jsonify(data)   
    
    # Add a new member to the Json file
    @app.route('/members', methods=['POST'])
    def add_member():
        with open("./data/dali_social_media.json", 'r') as file:
            members = json.load(file)

        new_member = request.json
        members.append(new_member)

        with open("./data/dali_social_media.json", 'w') as file:
            json.dump(members, file, indent=4)

        return jsonify({"message": "New member added successfully", "newMember": new_member}), 201


    @app.route('/members/<member_name>', methods=['GET'])
    def get_member_name(member_name):
        member = search_by_name(member_name)

        if member:
            return jsonify(member)
        else:
            return jsonify({'error': 'Member not found'}), 404
        
    

    
def stat_routes(app):
    @app.route('/stat/majors', methods=['GET'])
    def get_majors():
        major_count = {}
        for member in data:
            if member['major'] in major_count:
                major_count[member['major']] += 1
            else:
                major_count[member['major']] = 1

        return jsonify(major_count)
    
    @app.route('/stat/states', methods=['GET'])
    def get_states():
        state_count = {}
        for member in data:
            if member['home'].split()[1] in state_count:
                state_count[member['home'].split()[1]] += 1
            else:
                state_count[member['home'].split()[1]] = 1

        return jsonify(state_count)
    
    @app.route('/stat/years', methods=['GET'])
    def get_years():
        year_count = {}
        for member in data:
            if member['year'] in year_count:
                year_count[member['year']] += 1
            else:
                year_count[member['year']] = 1

        return jsonify(year_count)
    
    @app.route('/stat/birth-month', methods=['GET'])
    def get_birth_month():
        month_count = {}
        for member in data:
            month = member['birthday'].split('-')[0]
            if month in month_count:
                month_count[month] += 1
            else:
                month_count[month] = 1

        return jsonify(month_count)
    
    @app.route('/stat/top-dart-tradition', methods=['GET'])
    def get_fav_dartmouth_tradition():
        tradition = [member['favorite dartmouth tradition'] for member in data]
  
        
        bigram_counts = get_bigrams(tradition)
        top_bigrams = bigram_counts.most_common(20)
        bigrams_json = [{" ".join(bigram): frequency} for bigram, frequency in top_bigrams]

   
        return jsonify(bigrams_json)
    
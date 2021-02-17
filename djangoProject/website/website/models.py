from django.db import models

from SPARQLWrapper import SPARQLWrapper2

class SPARQL_Model:
    def get_generes(self):
        sparql = SPARQLWrapper2("http://localhost:3030/disease/sparql")
        sparql.setQuery("""
           PREFIX di: <urn:absolute:www.disease.com#>
            SELECT ?name ?age
            WHERE {
            ?x di:age ?age.
            ?x di:first_name ?name
            }""")
        return sparql.query().bindings

    def get_languages(self):
        sparql = SPARQLWrapper2("http://localhost:3030/disease/sparql")
        sparql.setQuery("""
           PREFIX di: <urn:absolute:www.disease.com#>
                    SELECT ?last
                        WHERE {
                            
                            ?name di:last_name ?last

        }
        """)
        return sparql.query().bindings

    def get_movies(self, language):
        sparql = SPARQLWrapper2("http://localhost:3030/disease/sparql")
        query = """PREFIX di: <urn:absolute:www.disease.com#>
         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                SELECT ?name 
                WHERE {
                     ?x rdf:type di:patient.
                        ?x di:prescription ?name.
                    
                         """
        query += "?x di:last_name '" + language + "'. }"


        sparql.setQuery(query)

        return sparql.query().bindings
    def get_disease(self):
        sparql = SPARQLWrapper2("http://localhost:3030/disease")
        query = """PREFIX di: <urn:absolute:www.disease.com#>
              SELECT ?disease
            WHERE {
           
            ?x di:disease_name ?diseas.
            BIND(REPLACE(STR(?diseas),"_"," ") AS ?disease) 
            
            }order by asc(?diseas)
"""
        sparql.setQuery(query)
        return sparql.query().bindings



    def get_diseaser(self,di):
        sparql = SPARQLWrapper2("http://localhost:3030/disease")
        query = """PREFIX di: <urn:absolute:www.disease.com#>
   select   ?city  where{
  ?x di:intensity ?intesity.
  ?x di:first_name ?fname.

BIND (
  IF(?intesity = 1, "needs more care",
    IF(?intesity = 2, "attention required",
      IF(?intesity = 3, "going serious",
        IF(?intesity = 4, "emergency case",
            
            "dead")
      )
    )
  ) AS ?result
  )
              bind( substr( str(?x), 30) as ?sub )        
                          """
        query += "?x di:disease_name '" + di + "'. " \
                                               " bind (concat(str(?sub),str(\" \"),str(?fname ), str(\" \"), str(?result) ) as ?city).  }"
        sparql.setQuery(query)
        return sparql.query().bindings


    def get_id(self):
        sparql = SPARQLWrapper2("http://localhost:3030/disease/sparql")
        sparql.setQuery("""
                 	  PREFIX di: <urn:absolute:www.disease.com#>
                            SELECT ?id
                                WHERE {
                                   
                                    ?name di:id ?id


                }
                """)
        return sparql.query().bindings

    def get_age(self):
        sparql = SPARQLWrapper2("http://localhost:3030/disease/sparql")
        sparql.setQuery("""
                         	 	 PREFIX di: <urn:absolute:www.disease.com#>
                                    SELECT ?age
                                        WHERE { 
                                            ?name di:age ?age.

                        }

                        """)
        return sparql.query().bindings
    def get_age2(self,ll):
        sparql = SPARQLWrapper2("http://localhost:3030/disease/sparql")
        query = """	PREFIX di: <urn:absolute:www.disease.com#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    SELECT  ?name
                    WHERE {

                         ?x di:first_name ?nam.
                           optional{ ?x di:last_name ?lname.}
                         ?x di:age ?age.
                        bind (concat(str(?nam), str(" "),str(?lname)) as ?name).
                                 """
        query += "filter(?age <=" + ll + "). }"

        sparql.setQuery(query)

        return sparql.query().bindings
    def get_place(self):
        sparql = SPARQLWrapper2("http://localhost:3030/disease/sparql")
        sparql.setQuery("""
                               	 	 PREFIX di: <urn:absolute:www.disease.com#>
                                   SELECT ?place
                                              WHERE {
                                                   ?x di:city ?place.

                              }

                              """)
        return sparql.query().bindings

    def get_idr(self, id):
        sparql = SPARQLWrapper2("http://localhost:3030/disease/sparql")
        query = """	PREFIX di: <urn:absolute:www.disease.com#>
                               PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                               SELECT ?name 
                               WHERE {
           	                ?x di:disease_name ?dname.
  ?x di:first_name ?fname.
  ?x di:last_name ?lname.
  ?x di:age ?age.
   bind (concat(str(?fname ), str(" ") ,str(?lname ), str("  have age "), str(?age ), str(" and disease name is "),str(?dname) ) as ?name).                                        """
        query += "?x di:id " + id + ". }limit 1"

        sparql.setQuery(query)

        return sparql.query().bindings

    def get_placer(self,pl):
        sparql = SPARQLWrapper2("http://localhost:3030/disease/sparql")
        query = """	PREFIX di: <urn:absolute:www.disease.com#>
                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                         SELECT DISTINCT ?name
                    WHERE {

                         ?x di:disease_name ?name.
                                
                                         """
        query += "?x di:city '" + pl + "'. }"

        sparql.setQuery(query)

        return sparql.query().bindings








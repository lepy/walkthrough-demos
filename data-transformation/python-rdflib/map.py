from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import XSD

csv="""obj_id,value,unit
1,520,MegaPA
2,550,MegaPA"""

g=Graph()

for row in csv.split("\n")[1:]:  # this is just an example; please use a proper CSV reader lib
	r=row.split(",")
	id = r[0]
	value = r[1]
	unit = r[2]

	# create the instance IRIs
	qual = URIRef("http://example.org/qual_" + id)
	proc = URIRef("http://example.org/proc_" + id)
	datum = URIRef("http://example.org/datum_" + id)
	spec = URIRef("http://example.org/spec_" + id)
	obj = URIRef("http://example.org/obj_" + id)
	role = URIRef("http://example.org/role_" + id)

	# IRIs from the ontology
	tensile_strength = URIRef("https://w3id.org/pmd/co/PMD_0080154")
	has_quality = URIRef("http://purl.obolibrary.org/obo/RO_0000086")
	has_role = URIRef("http://purl.obolibrary.org/obo/RO_0000087")
	has_value_specification = URIRef("http://purl.obolibrary.org/obo/OBI_0001938")
	specifies_value_of = URIRef("http://purl.obolibrary.org/obo/OBI_0001927")
	has_participant = URIRef("http://purl.obolibrary.org/obo/RO_0000057")
	specified_output_of = URIRef("http://purl.obolibrary.org/obo/OBI_0000312")
	realizes = URIRef("http://purl.obolibrary.org/obo/BFO_0000055")
	has_specified_numeric_value = URIRef("http://purl.obolibrary.org/obo/OBI_0001937")
	has_measurement_unit_label = URIRef("ttp://purl.obolibrary.org/obo/IAO_0000039")
	measurement_datum = URIRef("http://purl.obolibrary.org/obo/IAO_0000109")

	unit_iri = URIRef("http://qudt.org/vocab/unit/" + unit)

	# Add triples to the graph
	g.add((qual, RDF.type, tensile_strength))
	g.add((proc, has_participant, obj))
	g.add((datum, has_value_specification, spec))
	g.add((spec, has_specified_numeric_value, Literal(value)))
	g.add((obj, has_role, role))
	g.add((datum, RDF.type, measurement_datum))
	g.add((obj, specified_output_of, proc))
	g.add((spec, has_measurement_unit_label, unit_iri))
	g.add((proc, realizes, role))
	g.add((spec, specifies_value_of, qual))
	g.add((obj, has_quality, qual))


print (g.serialize(format="ttl"))


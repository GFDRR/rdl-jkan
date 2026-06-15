---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/geodata-of-mbera-refugee-camp-bassikounou-south-eastern-mauritania-december-10-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-mbera-refugee-camp-bassikounou-south-eastern-mauritania-december-10-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-mbera-refugee-camp-bassikounou-south-eastern-mauritania-december-10-2015
dataset_id: rdls_exp-mrt_unosat_geodatamberarefugeecampba_20151210
description: 'This map illustrates satellite-detected shelters and other buildings
  at the Mbera refugee camp in South Eastern Mauritania. As of 14 August 2015 a total
  of 11,327 shelters were detected, consisting of 497 administrative buildings, 2,968
  improvised shelters and 7,862 tent shelters. The camp covers a total of approximately
  415.01 hectares. A variety of clinics, nutrition centers, schools, and other important
  features are also identified on the map, and based on information from UNHCR. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-mbera-refugee-camp-bassikounou-south-eastern-mauritania-december-10-2015]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Satellite-detected shelter and building inventory at Mbera refugee
      camp, including tents, improvised shelters, and administrative structures
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery to detect shelter
    structures and buildings at Mbera refugee camp as of August 2015, classifying
    11,327 shelters by type (tents, improvised, administrative) and integrating UNHCR
    ground information on facility locations. The resulting geodataset provides a
    spatial inventory of camp infrastructure across 415 hectares.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: UNHCR
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-mbera-refugee-camp-bassikounou-south-eastern-mauritania-december-10-2015
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Mbera Refugee Camp, Bassikounou, South-Eastern Mauritania
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/ML/CE20120731MLI/Mbera_20150814_shp.zip
  format: null
  id: resource_0ec58188
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mbera_20150814_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Mbera Refugee Camp, Bassikounou, South-Eastern Mauritania
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/ML/CE20120731MLI/Mbera_20150814_gdb.zip
  format: null
  id: resource_bf5d894f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mbera_20150814_gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mrt_unosat_geodatamberarefugeecampba_20151210
spatial:
  bbox: null
  centroid: null
  countries:
  - MRT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-12-10'
temporal_resolution: null
title: Geodata of Mbera Refugee Camp, Bassikounou, South-Eastern Mauritania
version: null
vulnerability: null
---

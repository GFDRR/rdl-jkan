---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-goudoubou-refugee-camp-seno-province-burkina-faso-january-14-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-goudoubou-refugee-camp-seno-province-burkina-faso-january-14-2016
dataset_id: rdls_exp-bfa_unosat_geodatagoudoubourefugeeca_20160114
description: 'This map illustrates satellite detected shelters at the Goudoubou Refugee
  Camp in Seno Province, Burkina Faso, which hosts people from neighbouring Mali.
  As seen by the GeoEye-1 satellite on 30 October 2015, the camp contains a total
  of 2,669 structures within its 235.5 hectares. Of these structures, 476 are likely
  camp infrastructure buildings, 385 are improvised shelter structures, and 1,808
  are identified as tent shelters. This is a preliminary analysis and has not yet
  been validated in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-goudoubou-refugee-camp-seno-province-burkina-faso-january-14-2016]'
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
    description: Satellite-detected shelter structures at Goudoubou Refugee Camp classified
      by type (tents, improvised shelters, infrastructure buildings)
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts reviewed GeoEye-1 satellite imagery acquired on 30
    October 2015 and manually identified and classified 2,669 shelter structures within
    the Goudoubou camp boundary, categorizing them as tent shelters, improvised structures,
    or camp infrastructure buildings. The resulting spatial inventory was delivered
    as vector geodata (shapefile and geodatabase formats) with attribute fields documenting
    shelter counts, camp status, and area measurements.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-goudoubou-refugee-camp-seno-province-burkina-faso-january-14-2016
  rel: source
loss: null
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
  description: Geodata of Goudoubou Refugee Camp, Seno Province, Burkina Faso (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ML/CE20120731MLI/Goudoubou_20151030.shp.zip
  format: null
  id: resource_edfe5dcb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Goudoubou_20151030.shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Goudoubou Refugee Camp, Seno Province, Burkina Faso (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ML/CE20120731MLI/Goudoubou_20151030.gdb.zip
  format: null
  id: resource_754e603d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Goudoubou_20151030.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bfa_unosat_geodatagoudoubourefugeeca_20160114
spatial:
  bbox: null
  centroid: null
  countries:
  - BFA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-01-14'
temporal_resolution: null
title: Geodata of Goudoubou Refugee Camp, Seno Province, Burkina Faso
version: null
vulnerability: null
---

---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-minawao-refugee-settlement-far-north-province-cameroon-february-25-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-minawao-refugee-settlement-far-north-province-cameroon-february-25-2016
dataset_id: rdls_exp-cmr_unosat_geodataminawaorefugeesett_20160225
description: 'This map illustrates satellite-detected shelters and other buildings
  at the Minawao refugee settlement, Mayo-Tsanaga District, Far North Province in
  Cameroon as seen by the WorldView-2 satellite on 19 November 2015. UNOSAT analysed
  a total of 11,777 structures (9,390 tent shelters, 551 administrative buildings,
  634 improvised shelters, and 1,202 semi-permanent shelters) within 502 hectares
  of the settlement area. Previous analysis from 10 March 2015 indicated 5, 220 shelters
  over 261 hectares and thus the updated analysis indicates an increase of approximately
  126% on shelters and 93% in land occupied. Note that apparently adjoining, contiguous
  shelters were counted as a single shelter which may thus underestimate total number
  of shelters. This is a preliminary analysis & has not yet been validated in the
  field. Please send ground feedback to UNITAR/UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-minawao-refugee-settlement-far-north-province-cameroon-february-25-2016]'
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
    description: Satellite-detected shelter and building inventory at Minawao refugee
      settlement classified by structure type (tents, administrative, improvised,
      semi-permanent)
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
  description: UNOSAT analysts interpreted WorldView-2 satellite imagery acquired
    on 19 November 2015, manually detecting and classifying 11,777 structures by type
    (tents, administrative, improvised, semi-permanent) across the Minawao settlement.
    Multi-temporal comparison with 10 March 2015 imagery enabled trend analysis of
    settlement expansion.
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
- href: https://data.humdata.org/dataset/geodata-of-minawao-refugee-settlement-far-north-province-cameroon-february-25-2016
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
  description: Geodata of Minawao Refugee Settlement, Far North Province, Cameroon
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/NG/CE20140617NGA/CE20140617NGA_Minawao_20151119_shp.zip
  format: null
  id: resource_04db3fe3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140617NGA_Minawao_20151119_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Minawao Refugee Settlement, Far North Province, Cameroon
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/NG/CE20140617NGA/CE20140617NGA.gdb.zip
  format: null
  id: resource_e6616dd8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140617NGA.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-cmr_unosat_geodataminawaorefugeesett_20160225
spatial:
  bbox: null
  centroid: null
  countries:
  - CMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-02-25'
temporal_resolution: null
title: Geodata of Minawao Refugee Settlement, Far North Province, Cameroon
version: null
vulnerability: null
---

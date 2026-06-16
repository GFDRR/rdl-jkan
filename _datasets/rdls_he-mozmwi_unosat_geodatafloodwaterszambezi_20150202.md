---
attributions:
- entity:
    affiliation: null
    email: null
    name: Radarsat-2 satellite imagery
    url: https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-02-2015
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: World Population Database
    url: https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-02-2015
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-02-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-02-2015
dataset_id: rdls_he-mozmwi_unosat_geodatafloodwaterszambezi_20150202
description: 'This map illustrates satellite-detected flood waters in the Caia, Chemba,
  Mopeia and Mutarara and Morrumbala Districts of Mozambique and Nsanje District of
  southern Malawi along the Shire River as detected by Radarsat-2 imagery acquired
  30 January 2015. Between 21 January 2015 and 30 January 2015 waters receded from
  about 30,000 ha of lands but many areas along the Shire River remain affected. About
  22 villages are located within the flooded zone as of 30 January 2015 and according
  to the World Population data base around 25,000 people are located within these
  potentially affected a rea s. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-02-2015]'
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
    description: Approximately 25,000 people located within potentially affected areas
      along the Shire River
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Approximately 22 villages located within the flooded zone
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts reviewed and compared Radarsat-2 satellite imagery
    acquired on 30 January 2015 with baseline imagery to detect and delineate flood
    water extent across the Shire River region. Population exposure was estimated
    by overlaying the satellite-detected flood extent with World Population Database
    data to identify villages and estimate affected population within the flooded
    zone.
  sources:
  - id: source_1
    license: null
    name: Radarsat-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: World Population Database
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-02-2015
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
  description: Geodata of Flood Waters In Zambezia, Tete and Sofala, Mozambique, and
    Southern Region, Malawi (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20150112MOZ/FL20150112MOZ_shp.zip
  format: null
  id: resource_0088bce8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150112MOZ_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Waters In Zambezia, Tete and Sofala, Mozambique, and
    Southern Region, Malawi (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20150112MOZ/FL20150112MOZ.gdb.zip
  format: null
  id: resource_b818af68
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150112MOZ.gdb.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mozmwi_unosat_geodatafloodwaterszambezi_20150202
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  - MWI
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-02-02'
temporal_resolution: null
title: Geodata of Flood Waters In Zambezia, Tete and Sofala, Mozambique, and Southern
  Region, Malawi
version: null
vulnerability: null
---

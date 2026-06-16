---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-waters-as-of-12-november-2019-over-zongo-democratic-republic-of-the-congo
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-waters-as-of-12-november-2019-over-zongo-democratic-republic-of-the-congo
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-waters-as-of-12-november-2019-over-zongo-democratic-republic-of-the-congo
dataset_id: rdls_hzd-cod_unosat_detectedfloodwatersas12no_20191119
description: 'UNOSAT code: FL20191118COD This map illustrates satellite-detected floodedwaters
  along the Ubangui River over Zongo, Libenge Territory, Sud-Ubangi Territory in Democratic
  Republic of the Congo as observed from GeoEye-1 imagery acquired on 12 November
  2019. UNITAR-UNOSAT has identified 58 ha of potentially flood waters north-west
  of Zongo. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/flood-waters-as-of-12-november-2019-over-zongo-democratic-republic-of-the-congo]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed GeoEye-1 satellite imagery acquired on 12
    November 2019 and compared it with reference imagery to identify changes in water
    extent. Flooded areas were manually delineated and quantified (58 ha identified
    northwest of Zongo along the Ubangui River). The analysis is preliminary and field
    validation was pending.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-waters-as-of-12-november-2019-over-zongo-democratic-republic-of-the-congo
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
  description: Satellite-detected flood waters, as of 12 November 2019, over Zongo,
    Democratic Republic of the Congo (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CD/FL20191118COD/FL20191118COD_gdb.zip
  format: Geodatabase
  id: resource_8b0460db
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191118COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite-detected flood waters, as of 12 November 2019, over Zongo,
    Democratic Republic of the Congo (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CD/FL20191118COD/FL20191118COD_SHP.zip
  format: null
  id: resource_8e86f582
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191118COD_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-cod_unosat_detectedfloodwatersas12no_20191119
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-11-19'
temporal_resolution: null
title: Satellite-detected flood waters, as of 12 November 2019, over Zongo, Democratic
  Republic of the Congo
version: null
vulnerability: null
---

---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flooded-structures-as-of-15-november-2019-over-libenge-democratic-republic-of-the-congo
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flooded-structures-as-of-15-november-2019-over-libenge-democratic-republic-of-the-congo
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flooded-structures-as-of-15-november-2019-over-libenge-democratic-republic-of-the-congo
dataset_id: rdls_el-cod_unosat_detectedfloodedstructures_20191119
description: 'UNOSAT code: FL20191118COD This map illustrates satellite-detected flooded
  structures along the Ubangui River over Libenge, Libenge Territory, Sud-Ubangui
  Territory in Democratic Republic of the Congo as observed from Pleiades imagery
  acquired on 15 November 2019. UNITAR-UNOSAT identified 22 potentially flooded structures
  west of Libenge, within the extent of this map. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR -
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flooded-structures-as-of-15-november-2019-over-libenge-democratic-republic-of-the-congo]'
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
    description: Satellite-detected structures in the flooded area along the Ubangui
      River
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 15
    November 2019 over Libenge, Democratic Republic of the Congo, comparing it with
    reference imagery to identify structural changes indicative of flooding. Visual
    interpretation identified 22 potentially flooded structures along the Ubangui
    River, with results delivered as vector geodatabase and shapefile formats containing
    structure locations and areas.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flooded-structures-as-of-15-november-2019-over-libenge-democratic-republic-of-the-congo
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected flooded structures from post-event imagery analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Satellite-detected flooded structures, as of 15 November 2019, over
    Libenge, Democratic Republic of the Congo (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CD/FL20191118COD/FL20191118COD_gdb.zip
  format: Geodatabase
  id: resource_bdf966f3
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
  description: Satellite-detected flooded structures, as of 15 November 2019, over
    Libenge, Democratic Republic of the Congo (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CD/FL20191118COD/FL20191118COD_SHP.zip
  format: null
  id: resource_874b032b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191118COD_SHP.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-cod_unosat_detectedfloodedstructures_20191119
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
title: Satellite-detected flooded structures, as of 15 November 2019, over Libenge,
  Democratic Republic of the Congo
version: null
vulnerability: null
---

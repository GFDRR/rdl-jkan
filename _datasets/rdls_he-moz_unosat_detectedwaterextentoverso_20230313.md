---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-over-sofala-and-zambezia-provinces-mozambique-as-of-13-mar-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-over-sofala-and-zambezia-provinces-mozambique-as-of-13-mar-2023
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-sofala-and-zambezia-provinces-mozambique-as-of-13-mar-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-sofala-and-zambezia-provinces-mozambique-as-of-13-mar-2023
dataset_id: rdls_he-moz_unosat_detectedwaterextentoverso_20230313
description: 'UNOSAT code TC20230221MOZ, GDACS Id: 1000961 This map illustrates satellite-detected
  surface waters in Sofala and Zambezia Provinces, Mozambique as observed from an
  RCM-2 image acquired on 13 Mar. 2023 at 05:01 local time. Within the analyzed area
  of about 24,000 km2, about 900 km2 of land appear to be flooded. Based on Worldpop
  population data and the detected surface waters in the analyzed area, the potentially
  exposed population is mainly located in Zambezia province, including the district
  of Namacurra, with ~27,200 people, Nicoadala with ~22,500 people, and Cidade De
  Quelimane with ~ 15,600 people. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to United Nations Satellite
  Centre (UNOSAT). Important note: Flood analysis from radar images may underestimate
  the presence of standing waters in built-up areas and densely vegetated areas due
  to the backscattering properties of the radar signal.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/water-extent-over-sofala-and-zambezia-provinces-mozambique-as-of-13-mar-2023]'
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
    description: Potentially exposed population in Zambezia Province districts derived
      from WorldPop data overlaid with detected water extent
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed RCM-2 satellite imagery acquired on 13 March
    2023 to detect surface water extent through multi-temporal image comparison, identifying
    ~900 km2 of flooded land. Detected water polygons were overlaid with WorldPop
    population data to estimate potentially exposed populations in affected districts
    of Zambezia Province.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-over-sofala-and-zambezia-provinces-mozambique-as-of-13-mar-2023
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
  description: Satellite detected water extent over Sofala and Zambezia Provinces,
    Mozambique as of 13 Mar. 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3528/TC20230221MOZ_gdb.zip
  format: Geodatabase
  id: resource_f24b5d9a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Sofala and Zambezia Provinces,
    Mozambique as of 13 Mar. 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3528/TC20230221MOZ_shp.zip
  format: null
  id: resource_3f98c325
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ_shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_detectedwaterextentoverso_20230313
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-13'
temporal_resolution: null
title: Satellite detected water extent over Sofala and Zambezia Provinces, Mozambique
  as of 13 Mar. 2023
version: null
vulnerability: null
---

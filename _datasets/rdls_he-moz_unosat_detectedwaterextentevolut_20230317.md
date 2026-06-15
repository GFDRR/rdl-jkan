---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/water-extent-and-evolution-over-sofala-and-zambezia-provinces-mozambique-between-13-and-17
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-and-evolution-over-sofala-and-zambezia-provinces-mozambique-between-13-and-17
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-and-evolution-over-sofala-and-zambezia-provinces-mozambique-between-13-and-17
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-and-evolution-over-sofala-and-zambezia-provinces-mozambique-between-13-and-17
dataset_id: rdls_he-moz_unosat_detectedwaterextentevolut_20230317
description: 'UNOSAT code TC20230221MOZ, GDACS Id: 1000961 This map illustrates satellite-detected
  surface waters in Sofala and Zambezia Provinces, Mozambique as observed from a Sentinel-1
  image acquired on 17 Mar. 2023 at 03:09 local time. Within the analyzed area of
  about 27,000 km2, about 1,800 km2 of lands appear to be flooded. Water extent appears
  to have increased of about 900 km2 since the 13 March 2023. Based on Worldpop population
  data and the detected surface waters in the analyzed area, the potentially exposed
  population is mainly located in Zambezia province, including the district of Namacurra,
  with ~39,00 people, Nicoadala with ~32,000 people and Maganja Da Costa with ~ 23,000
  people. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to United Nations Satellite Centre (UNOSAT). Important
  note: Flood analysis from radar images may underestimate the presence of standing
  waters in built-up areas and densely vegetated areas due to backscattering properties
  of the radar signal.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-and-evolution-over-sofala-and-zambezia-provinces-mozambique-between-13-and-17]'
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
    description: Potentially exposed population in Sofala and Zambezia provinces derived
      from WorldPop data intersected with detected water extent
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
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-1 SAR images from 13 and 17 March 2023 were analyzed by UNOSAT
    through visual interpretation and change detection to delineate surface water
    extent in Sofala and Zambezia provinces. Detected water polygons were intersected
    with WorldPop population data to estimate potentially exposed population. The
    dataset provides post-event observed flood extent during Cyclone Freddy impacts
    in Mozambique.
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 SAR imagery
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
- href: https://data.humdata.org/dataset/water-extent-and-evolution-over-sofala-and-zambezia-provinces-mozambique-between-13-and-17
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
  description: Satellite detected water extent and evolution over Sofala and Zambezia
    Provinces, Mozambique between 13 and 17 March 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3537/TC20230221MOZ_gdb.zip
  format: Geodatabase
  id: resource_74919630
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
  description: Satellite detected water extent and evolution over Sofala and Zambezia
    Provinces, Mozambique between 13 and 17 March 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3537/TC20230221MOZ_shp.zip
  format: null
  id: resource_7678b913
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent and evolution over Sofala and Zambezia
    Provinces, Mozambique between 13 and 17 March 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3537/UNOSAT_Population_Exposure_TC20230221MOZ_Quelimane_17Mar2023.xlsx
  format: null
  id: resource_46544fce
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_TC20230221MOZ_Quelimane_17Mar2023.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_detectedwaterextentevolut_20230317
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
  start: '2023-03-17'
temporal_resolution: null
title: Satellite detected water extent and evolution over Sofala and Zambezia Provinces,
  Mozambique between 13 and 17 March 2023
version: null
vulnerability: null
---

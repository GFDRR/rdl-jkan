---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-over-kigali-city-southern-northern-western-and-eastern-provinces-rwanda-as-of
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-over-kigali-city-southern-northern-western-and-eastern-provinces-rwanda-as-of
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-kigali-city-southern-northern-western-and-eastern-provinces-rwanda-as-of
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-kigali-city-southern-northern-western-and-eastern-provinces-rwanda-as-of
dataset_id: rdls_he-rwa_unosat_detectedwaterextentoverki_20230505
description: 'UNOSAT code FL20230504RWA, GDACS Id: 1101977 This map illustrates satellite-detected
  surface waters in Kigali City, Southern, Northern, Western, and Eastern Provinces,
  Rwanda as observed from a Sentinel-1 image acquired on 3 May 2023 at 18:20 local
  time. Within the analyzed area of about 6,000 km2, about 20 km2 of land appear to
  be flooded. Based on Worldpop population data and the detected surface waters in
  the analyzed area, the potentially exposed population is mainly located in Southern
  Province Zambezia province with ~7,000 people, and Kigali City with ~5,600 people.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to United Nations Satellite Centre (UNOSAT). Important note:
  Flood analysis from radar images may underestimate the presence of standing waters
  in built-up areas and densely vegetated areas due to the backscattering properties
  of the radar signal.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-kigali-city-southern-northern-western-and-eastern-provinces-rwanda-as-of]'
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
    description: Potentially exposed population in Southern Province and Kigali City
      derived from WorldPop data intersected with detected water extent
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
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed Sentinel-1 SAR imagery acquired on 3 May\
    \ 2023 to detect surface water extent through comparative image analysis, identifying\
    \ approximately 20 km\xB2 of flooded area across 6,000 km\xB2 in Rwanda. Detected\
    \ water polygons were intersected with WorldPop gridded population data to estimate\
    \ potentially exposed populations in Southern Province and Kigali City."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-over-kigali-city-southern-northern-western-and-eastern-provinces-rwanda-as-of
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
  description: Satellite detected water extent over Kigali City, Southern, Northern,
    Western, and Eastern Provinces, Rwanda as of 3 May 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3573/FL20230304RWA_gdb.zip
  format: Geodatabase
  id: resource_21048f7d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230304RWA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Kigali City, Southern, Northern,
    Western, and Eastern Provinces, Rwanda as of 3 May 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3573/FL20230503RWA_SHP.zip
  format: null
  id: resource_ce212113
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230503RWA_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Kigali City, Southern, Northern,
    Western, and Eastern Provinces, Rwanda as of 3 May 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3573/PopulationExposure_FL20230503RWA_3May2023.xlsx
  format: null
  id: resource_04f34253
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PopulationExposure_FL20230503RWA_3May2023.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-rwa_unosat_detectedwaterextentoverki_20230505
spatial:
  bbox: null
  centroid: null
  countries:
  - RWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-05'
temporal_resolution: null
title: Satellite detected water extent over Kigali City, Southern, Northern, Western,
  and Eastern Provinces, Rwanda as of 3 May 2023
version: null
vulnerability: null
---

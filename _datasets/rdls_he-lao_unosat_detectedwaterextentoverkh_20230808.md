---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-over-khammouan-savannakhet-provinces-lao-pdr-as-of-04-august-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-over-khammouan-savannakhet-provinces-lao-pdr-as-of-04-august-2023
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-1
    url: https://data.humdata.org/dataset/water-extent-over-khammouan-savannakhet-provinces-lao-pdr-as-of-04-august-2023
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-khammouan-savannakhet-provinces-lao-pdr-as-of-04-august-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-khammouan-savannakhet-provinces-lao-pdr-as-of-04-august-2023
dataset_id: rdls_he-lao_unosat_detectedwaterextentoverkh_20230808
description: "UNOSAT code FL20230807LAO This map illustrates cumulative satellite-detected\
  \ surface waters over Khammouan & Savannakhet Provinces, Lao PDR as oberved from\
  \ a Sentinel-1 image acquired on 04 August 2023 at 18:04 local time. Within the\
  \ analysed area of about 25,000 km\xB2, a total of about 160 km\xB2 of lands appear\
  \ to be flooded. Based on Worldpop population data and the detected surface waters\
  \ in the analysed area, ~18,000 people are potentially exposed or living close to\
  \ flooded areas. This is a preliminary analysis and has not yet been validated in\
  \ the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Flood analysis from radar images may underestimate the\
  \ presence of standing waters in built-up areas and densely vegetated areas due\
  \ to backscaterring properties of the radar signal.. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/water-extent-over-khammouan-savannakhet-provinces-lao-pdr-as-of-04-august-2023]"
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
    description: Estimated population potentially exposed to or living close to flooded
      areas (~18,000 people) based on WorldPop population data intersected with detected
      flood extent
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
  - analysis_type: deterministic
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
  description: "Sentinel-1 SAR imagery acquired on 04 August 2023 was processed by\
    \ UNOSAT analysts to detect and delineate surface water extent across approximately\
    \ 25,000 km\xB2 in Khammouan and Savannakhet Provinces, Lao PDR. The detected\
    \ flood polygons were intersected with WorldPop population data to estimate the\
    \ number of people potentially exposed to flooding. The resulting geodatabase\
    \ and shapefile represent a preliminary, pre-field-validation flood extent product\
    \ for rapid emergency response."
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
  - id: source_3
    license: null
    name: Sentinel-1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-over-khammouan-savannakhet-provinces-lao-pdr-as-of-04-august-2023
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
  description: Satellite detected water extent over Khammouan & Savannakhet Provinces,
    Lao PDR as of 04 August 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3654/FL20230807LAO_gdb.zip
  format: Geodatabase
  id: resource_c8aa3b77
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230807LAO_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Khammouan & Savannakhet Provinces,
    Lao PDR as of 04 August 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3654/FL20230807LAO_SHP.zip
  format: null
  id: resource_ab8138cd
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230807LAO_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Khammouan & Savannakhet Provinces,
    Lao PDR as of 04 August 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3654/UNOSAT_Population_Exposure_FL20230807LAO_SavannakhetProvince_04Aug2023.xlsx
  format: null
  id: resource_9c6683db
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20230807LAO_SavannakhetProvince_04Aug2023.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-lao_unosat_detectedwaterextentoverkh_20230808
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-08-08'
temporal_resolution: null
title: Satellite detected water extent over Khammouan & Savannakhet Provinces, Lao
  PDR as of 04 August 2023
version: null
vulnerability: null
---

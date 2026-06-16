---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/water-extent-over-sylhet-mymensingh-dhaka-and-chattogram-divisions-bangladesh-as-of-26-may
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-over-sylhet-mymensingh-dhaka-and-chattogram-divisions-bangladesh-as-of-26-may
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-sylhet-mymensingh-dhaka-and-chattogram-divisions-bangladesh-as-of-26-may
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-sylhet-mymensingh-dhaka-and-chattogram-divisions-bangladesh-as-of-26-may
dataset_id: rdls_he-bgd_unosat_detectedwaterextentoversy_20220530
description: 'UNOSAT code: FL20220525BGD This map illustrates satellite-detected surface
  waters in Sylhet, Mymensingh, Dhaka, and Chattogram Divisions, Bangladesh as observed
  from a Sentinel-1 images acquired on 26 May 2022 at 05:47 local time and using an
  automated analysis with machine learning method. Within the analyzed area of about
  16,000 km2, about 6,800 km2 of lands appear to be flooded. In this area, about 5,400
  km2 of croplands and 1,270 km2 of herbaceous wetland appear to be likely affected
  by the flood waters. Based on Worldpop population data and the detected surface
  waters in the analyzed area, the potentially exposed population is mainly located
  in the district of Sunamganj with ~1,700,000 people and Sylhet with ~1,400,000 people.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to United Nations Satellite Centre (UNOSAT). Important note:
  Flood analysis from radar images may underestimate the presence of standing waters
  in built-up areas and densely vegetated areas due to backscattering properties of
  the radar signal.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-sylhet-mymensingh-dhaka-and-chattogram-divisions-bangladesh-as-of-26-may]'
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
    description: Cropland area affected by detected flood waters, approximately 5,400
      km2
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Herbaceous wetland area affected by detected flood waters, approximately
      1,270 km2
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Population exposed to detected flood waters based on WorldPop population
      data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_3
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
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 SAR imagery acquired on 26 May 2022 was processed using
    automated machine learning classification to detect surface water extent across
    16,000 km2 in four Bangladesh divisions. Detected water bodies were intersected
    with land use/land cover data to quantify affected cropland and wetland areas,
    and overlaid with WorldPop population grids to estimate exposed population. The
    resulting dataset provides post-event empirical flood extent observations for
    the May 2022 Bangladesh flooding event.
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
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-over-sylhet-mymensingh-dhaka-and-chattogram-divisions-bangladesh-as-of-26-may
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
  description: Satellite detected water extent over Sylhet, Mymensingh, Dhaka, and
    Chattogram Divisions, Bangladesh as of 26 May 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/BD/FL20220525BGD/FL20220525BGD_gdb.zip
  format: Geodatabase
  id: resource_57f7ea25
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220525BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Sylhet, Mymensingh, Dhaka, and
    Chattogram Divisions, Bangladesh as of 26 May 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/BD/FL20220525BGD/FL20220525BGD_SHP.zip
  format: null
  id: resource_302de1aa
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220525BGD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_unosat_detectedwaterextentoversy_20220530
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-05-30'
temporal_resolution: null
title: Satellite detected water extent over Sylhet, Mymensingh, Dhaka, and Chattogram
  Divisions, Bangladesh as of 26 May 2022
version: null
vulnerability: null
---

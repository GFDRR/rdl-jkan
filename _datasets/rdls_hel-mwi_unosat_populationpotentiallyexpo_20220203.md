---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/population-potentially-exposed-to-floods-in-malawi-as-of-26-and-31-january-and-2-february-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop spatial demographic data
    url: https://data.humdata.org/dataset/population-potentially-exposed-to-floods-in-malawi-as-of-26-and-31-january-and-2-february-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/population-potentially-exposed-to-floods-in-malawi-as-of-26-and-31-january-and-2-february-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/population-potentially-exposed-to-floods-in-malawi-as-of-26-and-31-january-and-2-february-
dataset_id: rdls_hel-mwi_unosat_populationpotentiallyexpo_20220203
description: 'UNOSAT code: TC20220126MWI This map illustrates population potentially
  exposed to floods (cumulative) aggregated by district in Malawi from Sentinel-1
  images acquired between 26 January and 2 February 2022 about 05:00 local time. The
  flood analysis was carried out by using automated analysis with an Artificial Intelligence
  based method, and Worldpop spatial demographic data. About 102,000 people were exposed
  or living close to flooded areas. The population potentially exposed to floods are
  mainly located in the districts of Chikwawa with ~ 33,700 people and Nsanje with
  ~ 33,700 people. This is a preliminary analysis and has not yet been validated in
  the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)
  . Important note: Flood analysis from radar images may underestimate the presence
  of standing waters in built-up areas and densely vegetated areas due to backscattering
  properties of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/population-potentially-exposed-to-floods-in-malawi-as-of-26-and-31-january-and-2-february-]'
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
    description: Population potentially exposed to or living close to flooded areas,
      aggregated by district
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 SAR imagery from 26 January to 2 February 2022 was processed
    using AI-based automated analysis to detect flood extent in Malawi. Detected inundation
    areas were intersected with WorldPop gridded population data to estimate population
    exposure by district. Results represent cumulative population potentially exposed
    to or living adjacent to flooded areas during the January 2022 cyclone event.
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
    name: WorldPop spatial demographic data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/population-potentially-exposed-to-floods-in-malawi-as-of-26-and-31-january-and-2-february-
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to floods from observed inundation extent in January-February
      2022 event
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
        metric: exposure
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
  description: Population potentially exposed to floods in Malawi as of 26 and 31
    January, and 2 February 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MW/TC20220126MWI/TC20220126MWI_gdb.zip
  format: Geodatabase
  id: resource_ca9cc654
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220126MWI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Population potentially exposed to floods in Malawi as of 26 and 31
    January, and 2 February 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MW/TC20220126MWI/TC20220126MWI_SHP.zip
  format: null
  id: resource_edfd988b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220126MWI_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mwi_unosat_populationpotentiallyexpo_20220203
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-02-03'
temporal_resolution: null
title: Population potentially exposed to floods in Malawi as of 26 and 31 January,
  and 2 February 2022
version: null
vulnerability: null
---

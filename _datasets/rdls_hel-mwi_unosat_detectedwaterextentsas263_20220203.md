---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-26-and-31-january-and-2-february-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop spatial demographic data
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-26-and-31-january-and-2-february-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-26-and-31-january-and-2-february-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-26-and-31-january-and-2-february-2022
dataset_id: rdls_hel-mwi_unosat_detectedwaterextentsas263_20220203
description: 'UNOSAT code: TC20220126MWI This map illustrates the floods (cumulative)
  aggregated using Sentinel-1 images acquired between 26 January and 2 February 2022
  about 05:00 local time. The flood analysis were carried out by using automated analysis
  with an Artificial Intelligence based method, and Worldpop spatial demographic data.
  About 102,000 people were exposed or living close to flooded areas. The population
  potentially exposed to floods are mainly located in the districts of Chikwawa with
  ~ 33,700 people and Nsanje with ~ 33,700 people. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to United
  Nations Satellite Centre (UNOSAT). Important note: Flood analysis from radar images
  may underestimate the presence of standing waters in built-up areas and densely
  vegetated areas due to backscattering properties of the radar signal.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-26-and-31-january-and-2-february-2022]'
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
    description: Population exposed or living close to flooded areas, primarily in
      Chikwawa and Nsanje districts
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-1 SAR imagery acquired over 8 days (26 Jan\xE2\u20AC\u201C\
    2 Feb 2022) was processed using AI-based automated water detection methods to\
    \ delineate cumulative flood extents. WorldPop gridded population data was overlaid\
    \ to estimate population exposure in affected districts. The resulting vector\
    \ geometries with area measurements represent post-event observed flood hazard."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-26-and-31-january-and-2-february-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to flood hazard from satellite-detected water
      extents
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
  description: Malawi - Satellite detected water extents as of 26 and 31 January,
    and 2 February 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MW/TC20220126MWI/TC20220126MWI_gdb.zip
  format: Geodatabase
  id: resource_3f872cce
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
  description: Malawi - Satellite detected water extents as of 26 and 31 January,
    and 2 February 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MW/TC20220126MWI/TC20220126MWI_SHP.zip
  format: null
  id: resource_b4a24b1a
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
slug: rdls_hel-mwi_unosat_detectedwaterextentsas263_20220203
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
title: Malawi - Satellite detected water extents as of 26 and 31 January, and 2 February
  2022
version: null
vulnerability: null
---

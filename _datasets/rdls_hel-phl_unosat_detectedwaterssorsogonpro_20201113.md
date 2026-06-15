---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/waters-in-sorsogon-province-bicol-region-of-philippines-as-of-13-november-2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/waters-in-sorsogon-province-bicol-region-of-philippines-as-of-13-november-2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-sorsogon-province-bicol-region-of-philippines-as-of-13-november-2020
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-sorsogon-province-bicol-region-of-philippines-as-of-13-november-2020
dataset_id: rdls_hel-phl_unosat_detectedwaterssorsogonpro_20201113
description: 'UNOSAT code: TC20201111PHL This map illustrates satellite-detected surface
  waters in Donsol and Pilar municipalities, Sorsogon province, Bicol region of Philippines
  as observed from a Sentinel-1 image acquired on 13 November 2020 at 05:30 local
  time. Within the analyzed area of about 180 km2, a total of about 3 km2 of lands
  appear to be flooded. The water extent appears to have receded of about 3 km2 since
  12 November 2020. Based on Worldpop population data and the detected surface waters,
  about 1,200 people are potentially exposed or living close to flooded areas. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR-UNOSAT. Important Note: Flood analysis from radar images
  may underestimate the presence of standing waters in built-up areas and densely
  vegetated areas due to backscattering properties of the radar signal.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/waters-in-sorsogon-province-bicol-region-of-philippines-as-of-13-november-2020]'
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
    description: Population potentially exposed or living close to detected flooded
      areas based on WorldPop data
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
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-1 SAR imagery acquired on 13 November 2020 was analyzed by\
    \ UNOSAT to detect surface water extent through comparison with baseline imagery.\
    \ Detected water polygons (~3 km\xC2\xB2) were intersected with WorldPop population\
    \ grids to estimate approximately 1,200 people potentially exposed to flooded\
    \ areas in Donsol and Pilar municipalities, Sorsogon province."
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
- href: https://data.humdata.org/dataset/waters-in-sorsogon-province-bicol-region-of-philippines-as-of-13-november-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to flooded areas detected by satellite
      imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  description: Satellite detected waters in Sorsogon province, Bicol region of Philippines
    as of 13 November 2020 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201111PHL/TC20201111PHL_gdb.zip
  format: Geodatabase
  id: resource_e2667617
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201111PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters in Sorsogon province, Bicol region of Philippines
    as of 13 November 2020 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201111PHL/TC20201111PHL_SHP.zip
  format: null
  id: resource_26bb2ab8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201111PHL_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-phl_unosat_detectedwaterssorsogonpro_20201113
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-13'
temporal_resolution: null
title: Satellite detected waters in Sorsogon province, Bicol region of Philippines
  as of 13 November 2020
version: null
vulnerability: null
---

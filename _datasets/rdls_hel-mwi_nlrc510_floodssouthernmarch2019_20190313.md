---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel 1
    url: https://data.humdata.org/dataset/floods-malawi-2019
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel 2
    url: https://data.humdata.org/dataset/floods-malawi-2019
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: High Resolution Settlement Layer (HRSL)
    url: https://data.humdata.org/dataset/floods-malawi-2019
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/floods-malawi-2019
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/floods-malawi-2019
dataset_id: rdls_hel-mwi_nlrc510_floodssouthernmarch2019_20190313
description: "For the floods in Southern Malawi of March 2019, we have combined flood\
  \ extent maps (Sentinel) with HRSL settlement/population grid. This results in a\
  \ calculation of # of affected buildings/people per district. The results is shared\
  \ through maps and in a shapefile. 1. Data sources Sentinel 1 Imagery from 7th of\
  \ March 2017 Sentinel 2 Imagery from 10th/12th/14th of March 2017 HRSL population\
  \ data Facebook Connectivity Lab and Center for International Earth Science Information\
  \ Network - CIESIN - Columbia University. 2016. High Resolution Settlement Layer\
  \ (HRSL). Source imagery for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed 9 March 2019.\
  \ 2. Good to know The flood extent for Nsanje district was separately added on March\
  \ 14th, to the existing flood extent for the main area from March 12th. 3. Methodology\
  \ A. Flood Extent Based on SAR The following steps were used to detect flood extent(water/no\
  \ water). In SNAP tool the raw data downloaded from sci-hub Copernicus was processed\
  \ to calibrate image for atmospheric correction, spike filter and terrain correction(This\
  \ is mainly for Sentinel 1 data). Finally defining water no water based on a threshold\
  \ applied on the corrected image. Defining a threshold is always a challenge in\
  \ SAR image analysis for flood detection, we collected data from the field to define\
  \ this threshold. For Sentinel 2 as a first step cloud filter was calculated by\
  \ applying a combined threshold on Band 2 and Band 10. The cloud mask shown in the\
  \ figure below didn't capture shadows of clouds, these were miss interpreted by\
  \ the flood algorithm as water/flood. To correct this areas with more cloud cover\
  \ were clipped out with a polygon. To define water no water based on sentinel data\
  \ we used NDWI index, the treshold is adjusted based on data collected from the\
  \ field Validation points were collected by Field team tested different values and\
  \ check if the threshold identified fits with observation. The complete methodology\
  \ how to detect flooding based on Sentinel 1 data and SNAP toolbox is documented\
  \ in ESA website. B. Affected People To calculate number of affected people per\
  \ each admin level, flood extent map is combined with HRSL population data. This\
  \ is done in two steps: First, in step 1, we calculate a raster, which multiplies\
  \ the population grid with the flood grid, such that we are left with only 'population\
  \ in flooded area'. This is done using raster calculator where population density\
  \ raster was multiplied by flood extent raster, which has a value of 0 for no flood\
  \ and 1 for flood areas. Note that the flood extent grid was first resampled to\
  \ match it to the population grid. This whole exercise is repeated for settlement/buildings\
  \ instead of population. Step 2: We apply zonal statistics per TA to calculate total\
  \ number of buildings/people affected in each admin level. For each Admin level2\
  \ estimated number of affected people and affected houses are plotted in the map.\
  \ The zonal statistics data used for plotting can be found in the shape file.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/floods-malawi-2019]"
details: null
exposure:
- asset_type:
    description: Building footprints and counts derived from High Resolution Settlement
      Layer (HRSL)
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
- asset_type:
    description: Residential population grid from High Resolution Settlement Layer
      (HRSL)
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Flood extent was mapped from Sentinel 1 and Sentinel 2 satellite imagery
    acquired during the March 2019 flooding event. The resulting flood extent polygons
    were spatially overlaid with the High Resolution Settlement Layer (HRSL) population
    and building footprint grid to calculate the number of affected buildings and
    people per administrative district (TA) in Southern Malawi.
  sources:
  - id: source_1
    license: null
    name: Sentinel 1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Sentinel 2
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: High Resolution Settlement Layer (HRSL)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/floods-malawi-2019
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Number of affected buildings per district from flood extent overlay
      with settlement layer
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
  - asset_category: population
    asset_dimension: population
    description: Number of affected people per district from flood extent overlay
      with population grid
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  description: TA shapefile with affected population (_popsum) and affected building
    (_setsum) included.
  download_url: https://data.humdata.org/dataset/3c378194-de05-4069-bec0-e6aa5106d11b/resource/3fddc60f-0668-41c6-a3b1-52e36aaed9da/download/ta_affected_population.zip
  format: null
  id: resource_3fddc60f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TA_affected_population.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Floods - Southern Malawi - March 2019 (A combined flood extent with
    data from march 7, 10 and 14th.)
  download_url: https://data.humdata.org/dataset/3c378194-de05-4069-bec0-e6aa5106d11b/resource/81bebfa6-70d0-4ed2-9c58-d749ee0ea6cb/download/flood_extent_march_2019.geojson
  format: null
  id: resource_81bebfa6
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: flood_extent_March_2019.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Map of affected population (population living in flooded area) per
    Traditional Authority.
  download_url: https://data.humdata.org/dataset/3c378194-de05-4069-bec0-e6aa5106d11b/resource/c1d0893f-32c3-4c41-a019-86a8f2e5ecc0/download/15march-affected_population.pdf
  format: null
  id: resource_c1d0893f
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 15march-affected_population.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 8 zoom-in maps per TA for the 8 worst hit TA's (affected population
    > 2000), showing an overlay of the flood extent and the settlement area.
  download_url: https://data.humdata.org/dataset/3c378194-de05-4069-bec0-e6aa5106d11b/resource/60f058be-8369-4d8e-9ace-76e17d65341f/download/15march-zoomin-per-ta.pdf
  format: null
  id: resource_60f058be
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 15march-zoomin-per-TA.pdf
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mwi_nlrc510_floodssouthernmarch2019_20190313
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
  start: '2019-03-13'
temporal_resolution: null
title: Floods - Southern Malawi - March 2019
version: null
vulnerability: null
---

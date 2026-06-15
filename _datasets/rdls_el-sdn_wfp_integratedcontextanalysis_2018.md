---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_sdn_2018
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_sdn_2018
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_sdn_2018
dataset_id: rdls_el-sdn_wfp_integratedcontextanalysis_2018
description: 'The ICA is a process of consultations supported by mapped-out data that
  produces a strategic plan describing where different combinations of programme themes
  are appropriate to achieve goals of reducing food insecurity and climate related
  shock risk. The ICA combines multi-year food security trends with natural shock
  risk data to highlight sub-national areas where different programme strategies make
  sense. Food security trend maps shows areas where safety nets can address regular
  food insecurity, and others where shocks make recovery more important. Climate-related
  natural shock risk maps show where DRR, preparedness and early warning efforts can
  complement food-security objectives. Atop this core foundation, mapped data on subjects
  including nutrition, gender, livelihoods and resilience can enrich theme-level strategic
  planning in which all pieces work together. The full group of ICA partners discuss
  these analytical results to arrive at strategic programmatic directions.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_sdn_2018]'
details: null
exposure:
- asset_type:
    description: Population distribution across livelihood zones and food security
      contexts
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
- asset_type:
    description: Agricultural livelihood zones and land degradation areas
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: The ICA integrates multi-year food security trend data (2010-2017)
    with natural shock hazard assessments (drought 1982-2017, flood 2013, land degradation
    2001-2013) and livelihood zone mapping to identify sub-national areas where different
    programme strategies are appropriate for reducing food insecurity and climate
    shock vulnerability.
  sources:
  - id: source_1
    license: null
    name: World Food Programme
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wfp_ica_sdn_2018
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecure population affected by drought-related shocks
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood events
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
  description: 'This layer contains information about the drought risk - by second-level
    administrative area - estimated during the Integrated Context Analysis (ICA) run
    in Sudan in 2018. Data source: HQ VAM Analysis of Chirps Rainfall Estimates (RFE),
    1982-2017. The main indicators used for the analysis were the number of poor growing
    seasons observed in the time window of interest and the inter-annual rainfall
    variability.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/629a00ccf3734697b5096e9066e66547/data
  format: null
  id: resource_83cb25bc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Drought Risk, 1982-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the numbers of food insecure
    people - by first-level administrative unit - estimated for the purposes of the
    Integrated Context Analysis (ICA) run in Mali in 2017. It should be noted that
    estimates of food insecure people were available only starting from 2014 onwards
    and, due to access constraints, some of the states were not covered by the survey.
    Data source: Integrated Phase Classification (IPC), 2014-2017. The main indicators
    used for the analysis were the percentage of food insecure population for long-term
    planning and the additional population figures in case of a major shock.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/eb893ff97148491cbe57d15cd73afb1e/data
  format: null
  id: resource_97a29017
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Estimated Numbers of Food Insecure People, 2014-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This document contains the results of the Integrated Context Analysis
    (ICA) conducted in Sudan in 2018. The analysis brings together the historical
    risk of natural shocks (floods and droughts) and the recurrence of high food insecurity
    with other key contextual information to provide broad programmatic strategies
    by second-level administrative area.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3a37b8b28c4c4193835658de942eeace/data
  format: null
  id: resource_efeabed5
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Technical Paper
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    - by second-level administrative area - observed for the purposes of the Integrated
    Context Analysis (ICA) run in Sudan in 2018. Data sources: HQ OSEP GIS Analysis
    of NASA MODIS 2001-2012, WorldClim 1970-2000, FAO and NASA SRTM Digital Elevation
    Model data. The main indicators used for the analysis were the average ecological
    changes observed between 2001-2005 and 2009-2013 and the percentage of erosion-prone
    surface.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3ada292015714c979f5af8ba94cd51d9/data
  format: null
  id: resource_79909f8e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Land Degradation, 2001-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the most predominant livelihood
    zones - by second-level administrative area - identified during the Integrated
    Context Analysis (ICA) run in Sudan in 2018. Data source: Fewsnet, 2011'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2a004d7acf974ef49d83c315e94ebb9e/data
  format: null
  id: resource_3b5783cb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Most Predominant Livelihood Zones, 2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the flood risk - by second-level
    administrative area - estimated during the Integrated Context Analysis (ICA) run
    in Sudan in 2018. Data sources: UNEP/UNISDR, GAR 2013. The main indicators used
    for the analysis were the percentage of district surface at flood risk and the
    maximum expected frequency of flood events with a 100-year return period.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2ad8d6bf4a444a659ef4762023a0b192/data
  format: null
  id: resource_57744663
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final categorization resulting
    from the Integrated Context Analysis (ICA) performed in Sudan in 2018, showing
    the areas of convergence of high levels of food insecurity recurrence and major
    propensity to natural shocks (floods and droughts).
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6c9f4067c8e74ccf8f63cb83b76bdfad/data
  format: null
  id: resource_171cc11b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the malnutrition levels - by
    second-level administrative unit - used for the purposes of the Integrated Context
    Analysis (ICA) run in Sudan in 2018. Data source: Simple Spatial Survey Method
    (S3M), 2013. The main indicators used for the analysis were the overall prevalences
    of stunting and wasting, with thresholds consistent with the guidelines suggested
    by the World Health Organization (WHO).'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/625d6c808a8c4816b6c65568fbfb49ac/data
  format: null
  id: resource_81db1425
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Prevalence of Malnutrition, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the food security trend analysis
    - by second-level administrative unit - used for the purposes of the Integrated
    Context Analysis (ICA) run in Sudan in 2018. Data source: Integrated Phase Classification
    (IPC), 2010-2017. The main indicator used for the analysis was the recurrence
    of IPC Phases 3 or above out of the number of available rounds.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a1511fdf8a6e4586b47a5fd3b7e1901d/data
  format: null
  id: resource_56d34748
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Recurrence of Food Insecurity, 2010-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This Excel file contains the food security analysis performed for the
    purposes of the Integrated Context Analysis (ICA) run in Sudan in 2018. The analysis,
    using the Integrated Phase Classification (IPC) data from 2010 through 2017, determines
    the recurrence of food insecurity conditions - by second-level administrative
    area - applying, as a threshold, the IPC Phase 3 (crisis).
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/1f37deba170f414bbcb48268d3eabf79/data
  format: null
  id: resource_b477f368
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Food Insecurity Recurrence Analysis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the natural shock risk (floods
    and droughts) estimated during the Integrated Context Analysis (ICA) performed
    in Sudan in 2018. Data sources: UNEP/UNISDR GAR 2013, HQ VAM Analysis of CHIRPS
    Rainfall Estimates (RFE) 1982-2017.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/84ef86d1475b481daa371a4002b2e021/data
  format: null
  id: resource_644934af
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Natural Shock Risk
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-sdn_wfp_integratedcontextanalysis_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: 'Sudan: Integrated Context Analysis (ICA), 2018'
version: null
vulnerability: null
---

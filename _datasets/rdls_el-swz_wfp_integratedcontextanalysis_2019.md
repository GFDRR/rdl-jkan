---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_swz_2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_swz_2019
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_swz_2019
dataset_id: rdls_el-swz_wfp_integratedcontextanalysis_2019
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_swz_2019]'
details: null
exposure:
- asset_type:
    description: Population density distribution across Eswatini in 2018
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
    description: Agro-ecological zones and livelihood zones in Eswatini
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
- asset_type:
    description: Land degradation and land cover change patterns from 2001-2016
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_3
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: The ICA combines multi-year food security trend data (2011-2019) with
    observed natural hazard data (flood extent from 2013, drought recurrence from
    1981-2018) and exposure layers (population density 2018, agro-ecological zones,
    land degradation 2001-2016) to identify sub-national areas where different programme
    strategies are appropriate for reducing food insecurity and climate shock risk.
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
- href: https://data.humdata.org/dataset/wfp_ica_swz_2019
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated number of food insecure people affected by drought shocks
      from 2011-2019
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
    description: Estimated number of additional food insecure people in case of major
      flood shock
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
  description: 'This layer contains information about the severity of natural hazards
    (floods and droughts) estimated during the Integrated Context Analysis (ICA) performed
    in Eswatini in 2019. Data sources: UNEP/UNISDR GAR 2013, HQ VAM Analysis of CHIRPS
    Rainfall Estimates (RFE) 1981-2018.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5ccc1c42ef3343dca4dbcb5c7054088a/data
  format: null
  id: resource_d856694b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Natural shocks hazard
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Eswatini: Integrated Context Analysis (ICA), 2019 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5a382b17dd2541d099b43d5e6fd8bde6/data
  format: PNG
  id: resource_4dacfd25
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Estimated number of additional food insecure people
    in case of a major shock, 2011-2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the flood hazard - by second-level
    administrative area - estimated during the Integrated Context Analysis (ICA) run
    in Eswatini in 2019. Data sources: UNEP/UNISDR GAR 2013. The main indicators used
    for the analysis were the percentage of district surface at flood risk and the
    maximum expected frequency of flood events with a 100-year return period.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/82546114a6af4fecb76a1b5178184241/data
  format: null
  id: resource_e7b5d1e3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Flood hazard, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final classification deriving
    from the Integrated Context Analysis (ICA) run in Eswatini in 2019, showing the
    areas of convergence between recurrence of food insecurity and propensity to natural
    shocks (floods and droughts).
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d355e9ad82d9493d8ec3facac02dab09/data
  format: null
  id: resource_b72c6597
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Eswatini: Integrated Context Analysis (ICA), 2019 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/9dd73b81ef8f436f9b36e049a874c0e6/data
  format: PNG
  id: resource_6e228862
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Estimated number of food insecure people for long-term
    planning, 2011-2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Eswatini: Integrated Context Analysis (ICA), 2019 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/915c67cc04934ccf9de3ea1578c3db35/data
  format: PNG
  id: resource_6169916c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Agro-ecological zones (2016) & Land Cover Change (2001-2016)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the recurrence of prevalence
    of stunting - by first-level administrative unit - used for the purposes of the
    Integrated Context Analysis (ICA) run in Eswatini in 2019. Data source: Eswatini
    Vulnerability Assessment and Analysis coordinated by the Eswatini Vulnerability
    Assessment Committee and the Central Statistics Office, 2009-2018. The key indicator
    used for the purposes of the analysis was the prevalence of stunting in children
    under the age of 5, with a threshold set at 20% because, according to the guidelines
    suggested by the World Health Organization (WHO), this is the break between the
    classes ''Medium'' and ''High''.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/865eda5227e04c64ad14127d9c984840/data
  format: null
  id: resource_1caf5f31
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Recurrence of prevalence of stunting, 2009-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Eswatini: Integrated Context Analysis (ICA), 2019 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/e2e61eaec4f04199a565603fddae90fc/data
  format: PNG
  id: resource_c282f2a0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - ICA Areas & Land Degradation, 2001-2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Eswatini: Integrated Context Analysis (ICA), 2019 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/99a33f566e2a4ad1a7c3fc5307d68caf/data
  format: PNG
  id: resource_887e4e11
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - ICA Areas & Population Density, 2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Eswatini: Integrated Context Analysis (ICA), 2019 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3798e470b3ef44b9a8f305e3fb74bc0b/data
  format: PNG
  id: resource_86b43c96
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Drought hazard, 1981-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This document contains the results of the Integrated Context Analysis
    (ICA) conducted in Eswatini in 2019. The analysis brings together the exposure
    of natural shocks (floods and droughts) and the recurrence of food insecurity
    with other key contextual information to provide broad programmatic strategies
    by second-level administrative area.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/92267ddaa8f6441cb162438e0c1a5b8e/data
  format: null
  id: resource_236a1e44
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Technical Paper
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Eswatini: Integrated Context Analysis (ICA), 2019 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/cce6660cb8724ba1b37ce1b60b987d28/data
  format: PNG
  id: resource_d725ae09
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - ICA Areas & Land Degradation (2001-2016) & Population
    Density (2018)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the most predominant livelihood
    zones - by second-level administrative area - identified during the Integrated
    Context Analysis (ICA) run in Eswatini in 2019. Data source: Eswatini VAC Livelihood
    Baseline Update, 2016.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2770a793844340eaa7e0ede6694c7211/data
  format: null
  id: resource_25a5a592
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Most predominant livelihood zones, 2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Eswatini: Integrated Context Analysis (ICA), 2019 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/8df9c9889bbf4d66afe01d6e56ae346a/data
  format: PNG
  id: resource_798c18f9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the numbers of food insecure
    people - by second-level administrative unit - estimated for the purposes of the
    Integrated Context Analysis (ICA) run in Eswatini in 2019. Data source: Eswatini
    Vulnerability Assessment and Analysis coordinated by the Eswatini Vulnerability
    Assessment Committee and the Central Statistics Office, 2011-2019. The main indicators
    used for the analysis were the percentage of food insecure population for long-term
    planning and the additional population figures in case of a major shock.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/24c8bdff532f4a3793ed749f6bc1eb9a/data
  format: null
  id: resource_938987ea
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Estimates of food insecure people, 2011-2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the food security trend analysis
    - by second-level administrative unit - used for the purposes of the Integrated
    Context Analysis (ICA) run in Eswatini in 2019. Data source: Eswatini Vulnerability
    Assessment and Analysis coordinated by the Eswatini Vulnerability Assessment Committee
    and the Central Statistics Office, 2011-2019. The key indicators used for the
    purposes of the analysis were the Food Consumption Score (FSC) and the Coping
    Strategy Index (CSI), with a threshold set at 20% because national average of
    food insecurity, throughout the available rounds, was found to be 18.75%.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2415e3b0cc19484c9f8b993199285e65/data
  format: null
  id: resource_63bac360
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Recurrence of food insecurity, 2011-2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the drought hazard - by second-level
    administrative area - estimated during the Integrated Context Analysis (ICA) run
    in Eswatini in 2019. Data source: HQ VAM Analysis of CHIRPS Rainfall Estimates
    (RFE), 1981-2015. The main indicator used for the analysis was the number of poor
    growing seasons observed in the time window of interest.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a088023bb9ec4469a3cc792bf38b1a90/data
  format: null
  id: resource_d091a153
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Drought hazard, 1981-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Eswatini: Integrated Context Analysis (ICA), 2019 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c08aebfe231849a8b21a5f2bda55209e/data
  format: PNG
  id: resource_a3d2471d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Flood hazard, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    - by second-level administrative area - observed for the purposes of the Integrated
    Context Analysis (ICA) run in Eswatini in 2019. Data sources: HQ OSE GIS Analysis
    of NASA MODIS 2001-2016, WorldClim 1970-2000, FAO and NASA SRTM Digital Elevation
    Model data. The main indicators used for the analysis were the average ecological
    changes observed between 2001-2006 and 2011-2016 and the percentage of erosion-prone
    surface.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/9c501d8f1d484524bddff9bc619f53d9/data
  format: null
  id: resource_3f1b8d52
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - Land Degradation, 2001-2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Eswatini: Integrated Context Analysis (ICA), 2019 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6965020ccfef47c0ab7ad8348b6e98a4/data
  format: PNG
  id: resource_3b12eef8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Eswatini, 2019 - ICA Areas & Recurrence of prevalence of stunting, 2009-2018
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-swz_wfp_integratedcontextanalysis_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - SWZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-12-31'
  start: '2019-01-01'
temporal_resolution: null
title: 'Eswatini: Integrated Context Analysis (ICA), 2019'
version: null
vulnerability: null
---

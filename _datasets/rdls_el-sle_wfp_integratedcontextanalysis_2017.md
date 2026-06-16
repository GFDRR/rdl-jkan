---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_sle_2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_sle_2017
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_sle_2017
dataset_id: rdls_el-sle_wfp_integratedcontextanalysis_2017
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_sle_2017]'
details: null
exposure:
- asset_type:
    description: Population density and food insecure population distribution across
      Sierra Leone
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
    description: Livelihood zones and agricultural areas subject to food insecurity
      recurrence
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
license: ODbL-1.0/
lineage:
  description: The ICA integrates multi-year food security trend data with natural
    shock risk assessments (flood and landslide) to identify sub-national areas where
    different programme strategies are appropriate. Food insecurity recurrence patterns
    are mapped against hazard risk layers to highlight areas where shocks drive vulnerability,
    informing WFP strategic planning for reducing food insecurity and climate-related
    shock risk.
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
- href: https://data.humdata.org/dataset/wfp_ica_sle_2017
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity recurrence linked to flood risk exposure
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
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity linked to landslide risk exposure
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: 'Sierra Leone: Integrated Context Analysis (ICA), 2017 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d210506599e6401fa2b73b48d545fe13/data
  format: PNG
  id: resource_1397e6fb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - ICA Areas & Land Degradation (2001-2012)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final categorization resulting
    from the Integrated Context Analysis (ICA) run in Sierra Leone in 2017. The final
    categorization shows areas of convergence between high recurrence of food insecurity
    and propensity to natural shocks
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a8db0f04f5f34369ad47ef6f8e190c88/data
  format: null
  id: resource_23c5e9ab
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the recurrence of food insecurity
    observed during the Integrated Context Analysis (ICA) run in Sierra Leone in 2017.
    Data souce: Comprehensive Food Security and Vulnerability Analysis (CFSVA) 2011-2015,
    Cadre Harmonise 2015-2017. It should be noted that two data sources, with different
    food security classification methodologies, have been used for the purposes of
    this analysis. The two main indicators used for the analysis were: - the poor
    Food Consumption Score, developed under the CFSVA, with a threshold set to 20%
    because it represents the national average according to the 2015 survey; - the
    number of times that an IPC Phase 3 or above was experienced in each district
    within the time window considered.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ef15a9ab7783422c848e3360766c88d9/data
  format: null
  id: resource_ae4b3dd8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Recurrence of Food Insecurity, 2011-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the malnutrition status estimated
    during the Integrated Context Analysis (ICA) run in Sierra Leone in 2017. Data
    sources: Standardized Monitoring and Assessment of Relief and Transition (SMART),
    2014. The main indicator used for the analysis was the prevalence of stunting
    in children aged below 5 years, classified according to the guidelines and thresholds
    suggested by the WHO. It should be noted that the data collection teams were unable
    to gather information for Bonthe and Kailahun districts because of restricted
    access caused by the Ebola Virus Disease (EVD) outbreak.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/aac4f95741604b45a889f5ea113ac9fd/data
  format: null
  id: resource_6aeb7b11
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Prevalence of Stunting, 2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    observed during the Integrated Context Analysis (ICA) run in Sierra Leone in 2017.
    Data source: HQ OSEP GIS Analysis of NASA MODIS, 2001-2012. The main indicators
    used for the analysis were the average land cover change observed within the time
    frame considered and the percentage of district erosion-prone surface.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f53ad7e317ed4a22acd5b40fb7386a13/data
  format: null
  id: resource_101d9f91
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the landslide risk estimated
    during the Integrated Context Analysis (ICA) run in Sierra Leone in 2017. Data
    sources: UNEP/UNISDR GAR 2013. The main indicators used for the analysis were
    the maximum expected frequency of landslide events with a 100-year return period
    and the percentage of district surface at landslide risk.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/8c2fa3e5fb8c49169ed240b4c88ac09e/data
  format: null
  id: resource_3156d4bf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Landslide Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Integrated Context Analysis (ICA), 2017 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/e7cffb6f6c8344f8a35f73c9d532fe65/data
  format: PNG
  id: resource_201dde22
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Recurrence of Food Insecurity, 2011-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Integrated Context Analysis (ICA), 2017 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/1e66eaa76ecc4843bcbad18dfa83f208/data
  format: PNG
  id: resource_d84492cf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Integrated Context Analysis (ICA), 2017 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/aa8bafe04a9b4b33beb8b82dff89736d/data
  format: PNG
  id: resource_d054f98b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - ICA Areas & Landslide Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Integrated Context Analysis (ICA), 2017 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4e2a7b8ac21b4a71baa8c0011df86ad7/data
  format: PNG
  id: resource_1ad4d583
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Integrated Context Analysis (ICA), 2017 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a74ea6bec96b4ed4901c08f02e50a41f/data
  format: PNG
  id: resource_649fe412
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - ICA Areas & Prevalence of Stunting, 2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Integrated Context Analysis (ICA), 2017 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/550d38bdb63f467ca481fb0f5b4d71d7/data
  format: PNG
  id: resource_a63a9cd6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Most Predominant Livelihood Zones, 2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Integrated Context Analysis (ICA), 2017 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/55e5e0b783624bdc95f0de129f5dd318/data
  format: PNG
  id: resource_ce75d39f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - ICA Areas & Confirmed Ebola Cases by District Population,
    2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the percentage of food insecure
    population - by third-level administrative unit - identified during the Integrated
    Context Analysis (ICA) run in Sierra Leone in 2017. Data sources: Comprehensive
    Food Security and Vulnerability Analysis (CFSVA), 2015. The key indicator used
    for the analysis was the percentage of total food insecure people based on the
    Consolidated Approach for Reporting Indicators of food security (CARI). Specifically,
    for the purposes of the ICA, the chiefdoms with more than 70% of food insecure
    people have been mapped on top of the ICA Areas and Categories.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2a053e105874402aab208b423dd3a3e5/data
  format: null
  id: resource_203fb335
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Recently Food Insecure Population, 2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Integrated Context Analysis (ICA), 2017 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/edb1c46509064644821cd884c79cd907/data
  format: PNG
  id: resource_290d7f3f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This document contains the results of the Integrated Context Analysis
    (ICA) conducted in Sierra Leone in 2017. The analysis brings together the historical
    flood risk and the recurrence of high food insecurity with other key contextual
    information to provide broad programmatic strategies by second-level administrative
    area.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6b7f46e962534373b534fa0f8e86546d/data
  format: null
  id: resource_8b1739fe
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Technical Paper
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Integrated Context Analysis (ICA), 2017 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ec18b1172a204b4a91bc63abae982f58/data
  format: PNG
  id: resource_51678e49
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - ICA Areas & Recent High Food Insecurity by Chiefdom,
    2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the flood risk estimated during
    the Integrated Context Analysis (ICA) run in Sierra Leone in 2017. Data source:
    UNEP/UNISDR GAR 2013, EMDAT 1996-2015. The main indicators used for the analysis
    were the percentage of district surface at flood risk and the historical frequency
    of flood events.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4bf273c169414891a27c4c0fd29b8cab/data
  format: null
  id: resource_25655566
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Integrated Context Analysis (ICA), 2017 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6d37aa56bf3e46f3abdc877454934d19/data
  format: PNG
  id: resource_a09c430d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - ICA Areas & Population Density, 2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This Excel file contains the food security analysis performed for\
    \ the purposes of the Integrated Context Analysis (ICA) run in Sierra Leone in\
    \ 2017. The analysis, using the Comprehensive Food Security Vulnerability Assessment\
    \ (CFSVA) and the Cadre Harmonis\u221A\xA9 data from 2011 to 2017, determines\
    \ the recurrence of food insecurity conditions - by second-level administrative\
    \ area - applying different thresholds: The two main indicators used for the analysis\
    \ were: - the poor Food Consumption Score, developed under the CFSVA, with a threshold\
    \ set to 20% because it represents the national average according to the 2015\
    \ survey; - the number of times that an IPC Phase 3 or above was experienced in\
    \ each district within the time window considered."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/fae3606a96e94d079ba58fbcb773dfe8/data
  format: null
  id: resource_67469f6a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Food Insecurity Recurrence Analysis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This Excel file contains the Food Consumption Score (FCS) by third-level
    administrative area used for the purposes of the Integrated Context Analysis (ICA)
    run in Sierra Leone in 2017. The analysis, using the Comprehensive Food Security
    Vulnerability Assessment (CFSVA) data from 2015, determines which chiefdoms have
    more than 70% of their population in food insecurity conditions.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/9ac271e1e22c4b4eb15331a16d2b2844/data
  format: null
  id: resource_42dc4e21
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Food Consumption Score (FCS) by Chiefdom
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the most predominant livelihood
    zones - by second-level administrative unit - identified during the Integrated
    Context Analysis (ICA) run in Sierra Leone in 2017. Data sources: Fewsnet, 2016.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b5c2faa078fa4b4798cca70feb631b58/data
  format: null
  id: resource_0d29e78b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Most Predominant Livelihood Zones, 2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the confirmed number of ebola
    cases by district (second-level administrative unit) population identified for
    the Integrated Context Analysis (ICA) run in Sierra Leone in 2017. Data sources:
    World Health Organization (WHO), 2015.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/509fae9946604486b6c6643d1df54b11/data
  format: null
  id: resource_f0d6758a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sierra Leone, 2017 - Confirmed Ebola Cases, 2015
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-sle_wfp_integratedcontextanalysis_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - SLE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Sierra Leone: Integrated Context Analysis (ICA), 2017'
version: null
vulnerability: null
---

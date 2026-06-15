---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_lso_2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_lso_2015
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_lso_2015
dataset_id: rdls_el-lso_wfp_integratedcontextanalysis_2015
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_lso_2015]'
details: null
exposure:
- asset_type:
    description: Population figures for 2011 with projections, mapped at sub-national
      administrative levels
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
    description: Predominant livelihood zones classified by agricultural and pastoral
      activities
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Ecological change indices and land degradation status across the
      country
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_3
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: The ICA combines multi-year food security trends (2010-2015) with natural
    shock risk data derived from observed flood (2013), drought (1998-2013), and land
    degradation patterns (2001-2012) to produce a strategic analysis of sub-national
    vulnerability. Population and livelihood zone data are spatially integrated with
    hazard observations to identify areas where different programme interventions
    are appropriate for reducing food insecurity and climate shock risk.
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
- href: https://data.humdata.org/dataset/wfp_ica_lso_2015
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity recurrence patterns linked to drought shocks from
      2010-2015
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
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population exposure to flood risk in 2013
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
  - asset_category: population
    asset_dimension: population
    description: Population exposure to drought risk from 1998-2013
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_3
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
  description: 'This layer contains information about the population figures by province
    (admin 1) used in the Integrated Context Analysis (ICA) run in Lesotho in 2015.
    Data source: Lesotho Bureau of Statistic, 2011.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/e63376c9a6ec4864b6d953d0cd7ff212/data
  format: null
  id: resource_a3d0e684
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Population Figures, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the food insecurity recurrence
    estimated during the Integrated Context Analysis (ICA) run in Lesotho in 2015.
    Data source: Lesotho Vulnerability Assessment Committee (LVAC) 2011-2015, Community
    and Household Surveillance (CHS) 2010-2015. The key indicator used for the analysis
    was the recurrence of food insecurity, with the threshold set to 20% of the province
    population.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c738b88413de4e6b8e5aad4ef2c6e6e8/data
  format: null
  id: resource_64e3a9d0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Recurrence of Food Insecurity, 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/32f42c927846415c92ab347658fc5779/data
  format: PNG
  id: resource_85026863
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Natural Shocks Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/015ab834e67b4120b99f675389aa7f68/data
  format: PNG
  id: resource_8a37d88f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - ICA Categories & Medium-High Negative Ecological Change
    (2001-2012)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3935d1b958c24ce396afde97fcb83b9d/data
  format: PNG
  id: resource_f231f66c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Predominant Livelihood Zones (2014), Negative Ecological
    Changes (2001-2012) & Settlements by ICA Category
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the flood risk estimated during
    the Integrated Context Analysis (ICA) run in Lesotho in 2015. Data source: UNEP/UNISDR
    GAR 2013. The key indicator used for the analysis was the percentage of surface
    area at risk of flooding.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2bbf6d0dd2c94a19bfe5b46889fc3f34/data
  format: null
  id: resource_459d1567
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the combined natural shocks
    risk (floods and droughts) estimated during the Integrated Context Analysis (ICA)
    run in Lesotho in 2015. Data source: UNEP/UNISDR GAR 2013, HQ VAM Analysis of
    NDVI data, 1998-2013.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c77c29f2aade4535bc9b5fe2184973bb/data
  format: null
  id: resource_11734d67
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Natural Shocks
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/33b5294ea83946e4a777c94e99f43797/data
  format: PNG
  id: resource_9b8fd634
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the drought risk estimated during
    the Integrated Context Analysis (ICA) run in Lesotho in 2015. Data source: HQ
    VAM Analysis of NDVI data, 1998-2013. The key indicator used for the analysis
    was the average number of drought events.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4e322a0055f442f3b3d9d33a058776ff/data
  format: null
  id: resource_d4dee467
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Drought Risk, 1998-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/0744e059c6304fc1b5ea5bfb4b250e08/data
  format: PNG
  id: resource_52f98f9e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Drought Risk, 1998-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/deca6e72ed6b4921bdbb992bb9a9e4ee/data
  format: PNG
  id: resource_95d0de79
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Projected Population Figures, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3854375ac3e749b0933e6d9deaab5755/data
  format: PNG
  id: resource_024fd4a0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Recurrence of Food Insecurity, 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3c4b8574e030438e9f596c1b64e2a3bd/data
  format: PNG
  id: resource_f83e4504
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - ICA Areas, Negative Ecological Changes (2001-2012) &
    High Population Density (2013)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/e5c02727137d4b3d8c9f6350b73da28b/data
  format: PNG
  id: resource_ce35da87
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Population Density, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    observed during the Integrated Context Analysis (ICA) run in Lesotho in 2015.
    Data source: NASA MODIS 2001-2012. The key indicator used for the analysis was
    the average ecological changes observed between 2001 and 2012 through remotely
    sensed data. It should be noted that the land degradation analysis consisted of
    an erosion propensity estimation, but given the low percentages of province surface
    erosion-prone, the map was not included in the final report.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/da33a01cf29b436aa704fc7697f8a061/data
  format: null
  id: resource_99e27945
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f5dab94cf2da4f43bac59525fc914774/data
  format: PNG
  id: resource_ce461347
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7bba1a3b240744f99f2e39ec367b9eac/data
  format: PNG
  id: resource_081e0707
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Average Ecological Change, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4b6d04611df44ad4bf30a9bb57055f38/data
  format: PNG
  id: resource_83acf978
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - ICA Areas & Medium-High Ecological Changes (2001-2012)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the predominant livelihood zone
    by province (Admin 1) identified during the Integrated Context Analysis (ICA)
    run in Lesotho in 2015. Data source: Fewsnet, 2014.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/36bf9ea8704043af8bfd73a9a3438e66/data
  format: null
  id: resource_5991f6ac
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Predominant Livelihood Zones, 2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This report contains the findings of the 2015 Integrated Context Analysis
    (ICA) conducted in Lesotho. The analysis brings together the historical risk of
    natural shocks (floods and drought) and the recurrence of high food insecurity
    with other key contextual information to provide broad programmatic strategies
    at district-level based on each district profile.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5ca3705511e74c6bb1b4af43fab10623/data
  format: null
  id: resource_db9c28e0
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Technical Paper and Programmatic Recommendations
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the main human settlements,
    codified with the ICA Category of their relative province, used during the Integrated
    Context Analysis (ICA) run in Lesotho in 2015. Data source: Global Discovery,
    2007.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/73dd91b931d548a38de9f31f5ed3c8c0/data
  format: null
  id: resource_722cf620
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Human Settlements, 2007
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final categorization deriving
    from the Integrated Context Analysis (ICA) run in Lesotho in 2015, showing areas
    of convergence between recurrence of food insecurity and propensity to natural
    shocks.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/49cefa69bd794559a59097e7cd22e04f/data
  format: null
  id: resource_10788627
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This Excel file contains the food security analysis performed for the
    purposes of the Integrated Context Analysis (ICA) run in Mozambique in 2017. The
    analysis, using the Community and Households Surveillance (CHS) and the Lesotho
    Vulnerability Assessment Committee (LVAC) data from 2010 to 2015, determines the
    recurrence of food insecurity conditions - by second-level administrative area
    - applying a threshold equal to 20%.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c13c6bd0637a496ab648db2c6d4bb32e/data
  format: null
  id: resource_e1b124a9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Lesotho, 2015 - Food Insecurity Recurrence Analysis
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-lso_wfp_integratedcontextanalysis_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - LSO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-12-31'
  start: '2015-01-01'
temporal_resolution: null
title: 'Lesotho: Integrated Context Analysis (ICA), 2015'
version: null
vulnerability: null
---

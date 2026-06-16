---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_zwe_2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_zwe_2015
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_zwe_2015
dataset_id: rdls_el-zwe_wfp_integratedcontextanalysis_2015
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_zwe_2015]'
details: null
exposure:
- asset_type:
    description: Food insecure population distribution mapped for long-term planning
      purposes
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
      systems
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
  description: The ICA combines multi-year food security trends (2009-2013) with natural
    shock risk data derived from historical flood (2013) and drought (1998-2013) occurrence
    records, integrated with livelihood zone mapping and tree cover loss data to produce
    sub-national risk stratification for programme planning in Zimbabwe.
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
- href: https://data.humdata.org/dataset/wfp_ica_zwe_2015
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity recurrence linked to drought shocks, 2009-2013
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
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity linked to flood risk exposure
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
  description: 'Zimbabwe: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/233e363f8a5f41b68e197717d41ca280/data
  format: PNG
  id: resource_b44355b6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - Predominant Livelihood Zones (2012) & High Tree Cover
    Loss (2000-2012)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zimbabwe: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/85478a549b7c4c318da48a270fc62eb6/data
  format: PNG
  id: resource_7687fdce
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - Natural Shocks Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the flood risk estimated during
    the Integrated Context Analysis (ICA) run in Zimbabwe in 2015. Data source: UNEP/UNISDR
    Global Assessment of Risk (GAR), 2013. The key indicator used was the percentage
    of flood affected areas.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7b752b3bd2fa429f8c8a7f9ef8c906f0/data
  format: null
  id: resource_7816233c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the estimated figures and percentages
    - by district population - of food insecure population resulting from the Integrated
    Context Analysis (ICA) run in Zimbabwe in 2015. Data source: ZIMVAC, 2009-2013.
    The key indicators used for the analysis were figures and percentages of food
    insecure population, used for long-term planning'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f62573d2c0b24c3d861a75db1cffdec8/data
  format: null
  id: resource_f6fe10aa
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - Food Insecure Population for Long-Term Planning, 2009-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zimbabwe: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c74eb111f402420284805eccef41640d/data
  format: PNG
  id: resource_a8f0b3bf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zimbabwe: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6e9041c99b2b46099ee45fd6b6c64fce/data
  format: PNG
  id: resource_be54b02a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the predominant livelihood zones
    identified during the Integrated Context Analysis (ICA) run in Zimbabwe in 2015.
    Data source: Zimbabwe Country Office, 2012. The twenty-four main livelihood zones
    identified by the CO were reclassified into nine broad categories to make the
    visualization easier.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/19c5714d79fc4d8b9395a0bd9c1d844c/data
  format: null
  id: resource_d561dafc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - Predominant Livelihood Zones, 2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the recurrence of food insecurity
    calculated during the Integrated Context Analysis (ICA) run in Zimbabwe in 2015.
    Data source: ZIMVAC 2009-2013, Fewsnet 2009-2013. The key indicator used for the
    analysis was the recurrence of food insecurity among 20% or above of the population.
    The 20% threshold was set in order to represent 1 or more out of 5 households/people
    from the total district population as food insecure.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/35213a451b9d4817a7a752f49aa1f367/data
  format: null
  id: resource_c7583696
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - Recurrence of Food Insecurity, 2009-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the overall tree cover loss
    estimated during the Integrated Context Analysis (ICA) run in Zimbabwe in 2015.
    In absence of land degradation data, a deforestation analysis was performed using
    remotely sensed data as a proxy. Data source: Hansen/UMD/Google/USGS/NASA, 2000-2012.
    The key indicators used for the analysis were the district surface affected by
    tree cover loss and the percentage value compared to the total district area.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d82e10333fe44bc69fbbf33778fd5796/data
  format: null
  id: resource_98b4687b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - Tree Cover Loss, 2000-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This document contains the results of the 2015 Integrated Context Analysis
    (ICA) conducted in Zimbabwe. The analysis brings together the historical risk
    of natural shocks (floods and drought) and the recurrence of high food insecurity
    with other key contextual information to provide broad programmatic strategies
    at district-level based on each district profile.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7cd40a2e39814fd1b95280b44ce8a118/data
  format: null
  id: resource_4e63e408
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - Technical Paper & Programmatic Recommendations
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the drought risk estimated during
    the Integrated Context Analysis (ICA) run in Zimbabwe in 2015. Data source: Water
    Requirement Satisfaction Index (WRSI) 2000-2013, Normalized Difference Vegetation
    Index (NDVI) 1998-2012. The key indicators used were the frequency of poor growing
    seasons and the recurrence of WRSI below the threshold, set to 59% (percentage
    of district area where poorer crop performance is a result of water stress conditions).'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ec54dd271e4e45beb9c58e2a72d595a6/data
  format: null
  id: resource_2dbc28d4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - Drought Risk, 1998-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zimbabwe: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/55d1f0fb69c2461aafe96c403135ca03/data
  format: PNG
  id: resource_9c7d2a5d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - ICA Areas, High Population Density (2011) & High Tree
    Cover Loss (2000-2010)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the malnutrition levels observed
    during the Integrated Context Analysis (ICA) run in Zimbabwe in 2015. Data source:
    National Nutrition Survey (NNS), 2010. The key indicator used for the analysis
    was the prevalence of stunting in children aged under 5 years. The prevalence
    of wasting was not used as a malnutrition indicator for the purposes of this analysis
    because it was found within acceptable limits (GAM < 2.4%) all over the country.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/257904bdef5741dca97f3a54673b3356/data
  format: null
  id: resource_ccc0d52d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - Prevalence of Stunting, 2010
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final classification resulting
    from the Integrated Context Analysis (ICA) run in Zimbabwe in 2015, showing areas
    of convergence between high recurrence of food insecurity and propensity to natural
    shocks.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f2fe5e5232834114bb96a35e14541cf0/data
  format: null
  id: resource_87b1ce2a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the natural shocks (floods and
    droughts) risk estimated during the Integrated Context Analysis (ICA) run in Zimbabwe
    in 2015. Data source: UNEP/UNISDR GAR 2013, WRSI 2000-2013, NDVI 1998-2012.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/edf4ab495cd24b08831f337291c70405/data
  format: null
  id: resource_61ea9ce4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Zimbabwe, 2015 - Natural Shocks Risk
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-zwe_wfp_integratedcontextanalysis_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - ZWE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-12-31'
  start: '2015-01-01'
temporal_resolution: null
title: 'Zimbabwe: Integrated Context Analysis (ICA), 2015'
version: null
vulnerability: null
---

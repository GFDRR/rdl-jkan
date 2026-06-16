---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_ssd_2016
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_ssd_2016
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_ssd_2016
dataset_id: rdls_el-ssd_wfp_integratedcontextanalysis_2016
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_ssd_2016]'
details: null
exposure:
- asset_type:
    description: Total population distribution across South Sudan in 2011
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
    description: Livelihood zones and agricultural land use patterns mapped by predominant
      livelihood type
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
    description: Land degradation and inter-annual vegetation change patterns from
      1998-2014
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
license: ODbL-1.0/
lineage:
  description: The ICA integrates multi-year food security trends (2010-2015) with
    natural shock risk data (flood and drought hazards from 1998-2014) and population/livelihood
    exposure data to produce a strategic analysis identifying sub-national areas where
    different programme interventions are appropriate. Food insecurity recurrence
    patterns are cross-referenced with mapped hazard risks and livelihood zones to
    highlight vulnerability hotspots.
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
- href: https://data.humdata.org/dataset/wfp_ica_ssd_2016
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
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity recurrence and malnutrition linked to drought risk
      exposure
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
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
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c7858f57c23e4715822ae9aefaf0cdf6/data
  format: PNG
  id: resource_47d80b79
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Food Insecurity Seasonality, June 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4af5ae5441b543acadedf5f9aa9c2f8f/data
  format: PNG
  id: resource_397f99cd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Flood Risk, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c389f0fdeaa441fa9fb512fe019d6cfb/data
  format: PNG
  id: resource_10e08b19
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Recurrence of Food Insecurity, 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6187d738c474409aaab896871f026a5f/data
  format: PNG
  id: resource_44095a03
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Food Insecurity Seasonality, February 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/46bd55cb57af40eb9064bbc6d73ae462/data
  format: PNG
  id: resource_8b0f1ae5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Food Insecurity Seasonality, October 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/349f2e356c27457c9ba1ab6b968795b4/data
  format: PNG
  id: resource_0295e279
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the flood risk - by second-level
    administrative area - estimated during the Integrated Context Analysis (ICA) run
    in South Sudan in 2016. Data sources: UNEP/UNISDR GAR 2011. The main indicators
    used for the analysis were the percentage of district surface at flood risk and
    the maximum expected frequency of flood events with a 100-year return period.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7b8d41ed0e0d4bc8bde833ecfaf5fda1/data
  format: null
  id: resource_36584358
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Flood Risk, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/14ef8ee928e243eeab52aeec5f882657/data
  format: PNG
  id: resource_7515d422
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Land Degradation, 2010-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the natural shock risk (floods
    and droughts) estimated during the Integrated Context Analysis (ICA) performed
    in South Sudan in 2016. Data sources: UNEP/UNISDR GAR 2011, HQ VAM Analysis of
    NDVI data, 1998-2012.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/be8926782b714cc0a2cb0d2ff5aca102/data
  format: null
  id: resource_159c4e0c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Natural Shock Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the most predominant livelihood
    zones - by second-level administrative area - identified during the Integrated
    Context Analysis (ICA) run in South Sudan in 2016. Data source: Fewsnet, 2008.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/815155d9658341a99e7eb0402c8ca9f2/data
  format: null
  id: resource_168d0149
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Most Predominant Livelihood Zones, 2008
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the drought risk - by second-level
    administrative area - estimated during the Integrated Context Analysis (ICA) run
    in South Sudan in 2016. Data source: HQ VAM Analysis of NDVI data, 1998-2014.
    The main indicators used for the analysis were the most prelevant number of poor
    growing seasons and the percentage of surface area affected by one or more poor
    growing seasons.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ee8ce1c7235648138262bb8943553210/data
  format: null
  id: resource_1e9c5a38
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Drought Risk, 1998-2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c891b1db666a4eafb5f2e21b87fd6581/data
  format: PNG
  id: resource_fd4c1bf6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Total Population, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final categorization resulting
    from the Integrated Context Analysis (ICA), run in South Sudan in 2016, showing
    areas of convergence between high recurrence of food insecurity and high propensity
    to natural shocks (floods and droughts).
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/82e7820a46d4475986d5cffc50ca26db/data
  format: null
  id: resource_abd51044
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/de03710d5f9644faa5b0bba58de332c2/data
  format: PNG
  id: resource_cac6d1f1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Natural Shock Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the main human settlements ,
    codified by the ICA Categories of the relative second-level administrative area,
    used in the Integrated Context Analysis (ICA) run in South Sudan in 2016.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5416f010bf294c5b826b0fe532ef82d6/data
  format: null
  id: resource_8b40cd45
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - ICA-Coded Human Settlements
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/47c64ef30a3040d6847c88c58097ac4e/data
  format: PNG
  id: resource_67f1774c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Recurrence of Food Insecurity and Malnutrition, 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f71ce30648fe45b08005e49feb1a4e89/data
  format: PNG
  id: resource_59542fda
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Drought Risk, 1998-2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/90519bdb250b4d16a9299d1bb76a40b2/data
  format: PNG
  id: resource_14062f14
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Inter-Annual Vegetation Change (1998-2014) & ICA-Coded
    Settlements
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This document contains the results of the Integrated Context Analysis
    (ICA) conducted in South Sudan in 2016. The analysis brings together the historical
    risk of natural shocks (floods and droughts) and the recurrence of high food insecurity
    with other key contextual information to provide broad programmatic strategies
    by second-level administrative area.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/79eb4ea260234c33a7e3499587c02104/data
  format: null
  id: resource_0abafd25
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Technical Paper & Programmatic Recommendations
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    observed during the Integrated Context Analysis (ICA) performed in South Sudan
    in 2016. Data source: Regional Centre for Mapping of Resources for Development
    (RCMRD), 2010-2012. The main indicator used for the analysis was an average land
    degradation index, generated through a combination of factors such as land conformation,
    vegetation cover and quality, precipitation, soil type and erodibility, population
    density.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3fd393f4ab824ad69c034b9b556a5e7e/data
  format: null
  id: resource_d3218cc9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Land Degradation, 2010-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/29d7309c9d32483f8e66a7955a9ee827/data
  format: PNG
  id: resource_2510d41b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Most Predominant Livelihood Zones & ICA-Coded Settlements
    & Conflict Score
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/acfa660dbb8d4ab5973f4919e189de03/data
  format: PNG
  id: resource_8883f20d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Intra-Annual Vegetation Change (1998-2014) & ICA-Coded
    Settlements
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c08c5aad8ac944e9a72fb0e278c51d51/data
  format: PNG
  id: resource_783f1cf0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - ICA Areas & Land Degradation (2010-2012) & Population
    Density, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This Excel file contains the food security analysis performed for the
    purposes of the Integrated Context Analysis (ICA) run in South Sudan in 2016.
    The analysis, using the Food Security Monitoring System (FSMS) from 2010 to 2015,
    determines the recurrence of food insecurity conditions - by second-level administrative
    area - applying a threshold equal to 30%.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/dc1ed90be39f443586350599d105a30b/data
  format: null
  id: resource_ccd3f2dd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Food Insecurity Recurrence Analysis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the food insecurity levels estimated
    during the Integrated Context Analysis (ICA) run in South Sudan in 2016. Data
    source: Food Security Monitoring System (FSMS), 2010-2015. The food security threshold
    to determine the recurrence of food insecurity was set at 30% as only the best
    quantile had a value below 20% (which is the traditional mapping protocol) and
    that the value used was the sum of two categories (moderate and severe food insecurity).
    The key indicators used for the analysis were the recurrence above the threshold,
    the average against national average and variability/stability.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/48b49caa4d5f4581bb677923e67d0ae5/data
  format: null
  id: resource_78331b75
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Recurrence of Food Insecurity, 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the global acute malnutrition
    levels estimated during the Integrated Context Analysis (ICA) run in South Sudan
    in 2016. Data source: Food Security Monitoring System (FSMS), 2010-2015. The threshold
    to determine the recurrence of global acute malnutrition was set at 15% (emergency
    level). It should be noted that Mid-Upper Arm Circumference (MUAC) was used as
    a proxy to measure child malnutrition. The key indicators used for the analysis
    were the recurrence above the threshold, the average against national average
    and variability/stability.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f4c26003545b4aa7a2bbbad054d4758d/data
  format: null
  id: resource_23bfe008
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - Recurrence of Malnutrition, 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Integrated Context Analysis (ICA), 2016 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a7625734d5954287b8d88dfb9487d884/data
  format: PNG
  id: resource_bb7a6cbf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA South Sudan, 2016 - ICA Areas
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ssd_wfp_integratedcontextanalysis_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: 'South Sudan: Integrated Context Analysis (ICA), 2016'
version: null
vulnerability: null
---

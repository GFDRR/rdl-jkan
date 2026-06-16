---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_arm_2016
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_arm_2016
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_arm_2016
dataset_id: rdls_hl-arm_wfp_integratedcontextanalysis_2016
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_arm_2016]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: ODbL-1.0/
lineage:
  description: The ICA combines multi-year food security trend data (2010-2014) with
    natural shock risk assessments (2011-2015) at sub-national level to produce strategic
    vulnerability maps. Drought risk and food insecurity recurrence are spatially
    integrated to identify areas where different programme interventions are appropriate
    for reducing food insecurity and climate shock vulnerability.
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
- href: https://data.humdata.org/dataset/wfp_ica_arm_2016
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity recurrence linked to drought risk, 2010-2014
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
    description: Estimated numbers of food insecure people affected by drought shocks,
      2010-2014
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
  description: 'This layer contains information about the food insecurity recurrence
    and variability estimated during the Integrated Context Analysis (ICA) run in
    Armenia in 2016. Data source: Integrated Living Condition Surveys (ILCS), 2010-2014.
    The key indicator used is the food security classification developed under the
    Comprehensive Food Security Vulnerability and Nutrition Analysis (CFSVNA), considering
    a 15% threshold since only severe food insecurity was used for the analysis.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d0fffaac5dbd4cbbb84ea653ba1e0790/data
  format: null
  id: resource_a89a7723
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2016 - Food Insecurity Recurrence, 2010-2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the estimates of food insecure
    population for long-term planning and the additional food insecure people in case
    of a major shock. Data source: Integrated Living Condition Surveys (ILCS) 2010-2014.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/09c635e3c3434affbf290c1b5678750c/data
  format: null
  id: resource_d119f361
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2016 - Estimated Numbers of Food Insecure People, 2010-2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the drought risk estimated during
    the Integrated Context Analysis (ICA) run in Armenia in 2016. Data source: HQ
    VAM Analysis of CHIRPS Rainfall Estimates, 2011-2015. The key indicators used
    for the analysis were the percentage of surface affected by drought risk and the
    overall number of poor growing seasons.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/0ad666a1e8b142548c8cd930d7076c1f/data
  format: null
  id: resource_62149d3a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2016 - Drought Risk, 2011-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final classification deriving
    from the Integrated Context Analysis (ICA) run in Armenia in 2016, showing the
    areas of convergence between recurrence of food insecurity and propensity to natural
    shocks.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f3828b56b7c84bf584d762f467c15197/data
  format: null
  id: resource_0152ef2c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2016 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the risk of natural shocks (floods,
    mudflows and droughts) estimated during the Integrated Context Analysis (ICA)
    run in Armenia in 2016. Data source: UNEP/UNISDR GAR 2013, Armenia Hydrometeorological
    Monitoring Service 2012, HQ VAM Analysis of CHIRPS RFE 2011-2015.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a2a4a515f7e645fdab186c70b8b200b1/data
  format: null
  id: resource_e450a4a7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2016 - Natural Shocks Risk
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-arm_wfp_integratedcontextanalysis_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - ARM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: 'Armenia: Integrated Context Analysis (ICA), 2016'
version: null
vulnerability: null
---

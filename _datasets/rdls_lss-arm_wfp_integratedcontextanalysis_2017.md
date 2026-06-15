---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_arm_2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_arm_2017
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_arm_2017
dataset_id: rdls_lss-arm_wfp_integratedcontextanalysis_2017
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_arm_2017]'
details: null
exposure: []
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: The ICA combines multi-year food security trends (2010-2015) with natural
    shock risk data derived from historical hazard observations (drought 1981-2015,
    flood 2013, mudflow 2012, land degradation 2001-2012) to produce sub-national
    risk maps identifying areas where different programme strategies are appropriate
    for reducing food insecurity and climate-related shock vulnerability.
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
- href: https://data.humdata.org/dataset/wfp_ica_arm_2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated numbers of food insecure people affected by drought-related
      food insecurity from 2010-2015
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
    Armenia in 2017. Data source: Integrated Living Condition Surveys (ILCS), 2010-2015.
    The key indicator used is the food security classification developed under the
    Comprehensive Food Security Vulnerability and Nutrition Analysis (CFSVNA), considering
    a 15% threshold since only severe food insecurity was used for the analysis.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4f5e1c05aac54761b5855164de03d95f/data
  format: null
  id: resource_a909475d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2017 - Food Insecurity Recurrence & Variability, 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the mudflow risk estimated during
    the Integrated Context Analysis (ICA) run in Armenia in 2016. The results are
    still valid for the purposes of the ICA update performed in 2017. Data source:
    Armenia Hydrometeorological Monitoring Service, 2012. The key indicators used
    for the analysis are the percentage of mudflow affected area and the overall level
    of mudflow risk'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/35fa507117d04e49869a18589b2057ee/data
  format: null
  id: resource_216defa1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2016 & 2017 - Mudflow Risk, 2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the estimates of food insecure
    population for long-term planning and the additional food insecure people in case
    of a major shock. Data source: Integrated Living Condition Surveys (ILCS) 2010-2015.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/88db675b91c24fde8788ebeb64770c13/data
  format: null
  id: resource_b8742e81
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2017 - Estimated Numbers of Food Insecure People, 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This document, produced in HQ in collaboration with the Armenia CO,
    is the Technical Paper containing the final results of the Integrated Context
    Analysis (ICA) performed in 2017.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/cf20906d0ef243d6b6e31415eef84374/data
  format: null
  id: resource_269a102b
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia - Technical Paper, 2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the hail storm and frost risk
    estimated during the Integrated Context Analysis (ICA) run in Armenia in 2017.
    Data source: Armenia Hydrometeorological Monitoring Service, 2012. The key indicators
    used for the analysis were the number of hail storm days recorded per year and
    the overall level of frost risk.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2dd11935f48f4d0ab8c986014facf4cc/data
  format: null
  id: resource_750b59b7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2017 - Additional Hazards, 2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the overall risk of natural
    shocks estimated during the Integrated Context Analysis (ICA) run in Armenia in
    2017. Data source: UNEP/UNISDR GAR 2013, HQ VAM Analysis of CHIRPS RFE 1981-2015,
    Armenia HydroMeteorological Monitoring Service 2012.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/af266512a2cb4d9f92587ad0136944b4/data
  format: null
  id: resource_872c9957
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2017 - Natural Shocks Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the drought risk estimated during
    the Integrated Context Analysis (ICA) run in Armenia in 2017. Data source: HQ
    VAM Analysis of CHIRPS Rainfall Estimates, 1981-2015 (the time frame considered
    is considerably different compared to the one used in the 2016 ICA). The key indicator
    used is the number of poor growing seasons.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/44046ab0bd6e482cab2953f1387e421e/data
  format: null
  id: resource_07ab005f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2017 - Drought Risk, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    calculated during the Integrated Context Analysis (ICA) run in Armenia in 2016.
    The results are still valid for the purposes of the ICA update performed in 2017.
    Data source: HQ OSEP GIS Analysis of NASA MODIS 2001-2012. The key indicators
    used for the analysis were the average ecological change observed in the reference
    period and the percentage of surface prone to erosion.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/160e053e65b748d2bc0c2d02929e08eb/data
  format: null
  id: resource_fa3acca6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2016 & 2017 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the nutrition levels estimated
    during the Integrated Context Analysis (ICA) run in Armenia in 2016. The results
    are still valid for the purposes of the ICA update performed in 2017. Data source:
    Integrated Living Condition Surveys (ILCS) 2014. The key indicators used for the
    analysis were the prevalence of stunting and overweight in children below 5 years
    of age, considering respectively a 20% and a 15% percent threshold.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/8328c50094314cec832ec5cc2e1dc32d/data
  format: null
  id: resource_e8fdf36f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2016 & 2017 - Malnutrition, 2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final classification deriving
    from the Integrated Context Analysis (ICA) run in Armenia in 2017, showing the
    areas of convergence between recurrence of food insecurity and propensity to natural
    shocks.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d7a635d4a466478987ac37224b96e253/data
  format: null
  id: resource_f99e457e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2017 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the flood risk estimated during
    the Integrated Context Analysis (ICA) run in Armenia in 2016. The results are
    still valid for the ICA update performed in 2017. Data source: UNEP/UNISDR Global
    Assessment of Risk (GAR) 2013. The key indicators used for the analysis are the
    percentage of flood affected surface and the maximum expected frequency of flood
    events (with a 100-years return time period).'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4375ec7086614dd983a265c44529943f/data
  format: null
  id: resource_f5c06270
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Armenia, 2016 & 2017 - Flood Risk, 2013
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-arm_wfp_integratedcontextanalysis_2017
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
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Armenia: Integrated Context Analysis (ICA), 2017'
version: null
vulnerability: null
---

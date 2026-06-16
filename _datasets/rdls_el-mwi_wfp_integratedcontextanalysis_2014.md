---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_mwi_2014
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_mwi_2014
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_mwi_2014
dataset_id: rdls_el-mwi_wfp_integratedcontextanalysis_2014
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_mwi_2014]'
details: null
exposure:
- asset_type:
    description: Food insecure population by sub-national administrative areas
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
    description: Livelihood zones and land degradation patterns across Malawi
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
  description: The ICA combines multi-year food security trends (2009-2013) with historical
    natural shock risk data (drought 2004-2013, flood 2000-2013) and livelihood zone
    mapping to identify sub-national areas where different programme strategies are
    appropriate for reducing food insecurity and climate-related shock vulnerability.
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
- href: https://data.humdata.org/dataset/wfp_ica_mwi_2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecure population affected by drought risk
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
    description: Food insecure population affected by flood risk
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
  description: 'This layer contains information about the land degradation phenomenon
    observed during the Integrated Context Analysis (ICA) run in Malawi in 2014. Data
    source: European Space Agency, 1990-2010. Local land degradation data were not
    available for the purposes of this analysis, therefore a deforestation analysis
    was performed using remotely sensed land cover data. The key indicators used for
    the analysis were the percentage and the overall surface of vegetation cover loss.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2920f1c0246a425ba561b8202fa0e559/data
  format: null
  id: resource_48170247
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - Land Degradation, 1990-2010
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final categorization resulting
    from the Integrated Context Analysis (ICA) run in Malawi in 2014, showing areas
    of convergence between recurrence of food insecurity and high propensity to natural
    shocks.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/233c5d55b0ef49e99582b8447850a1f2/data
  format: null
  id: resource_56b9cf5c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This report contains the findings of the 2014 Integrated Context Analysis
    (ICA) conducted in Malawi. The analysis brings together the historical risk of
    natural shocks (floods and drought) and the recurrence of high food insecurity
    with other key contextual information (like vegetation loss used as a proxy for
    land degradation) to provide broad programmatic strategies at district-level based
    on each district profile.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/0a90f0c9b0cd411fb93479ceb2f93eed/data
  format: null
  id: resource_fe4dcf1e
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - Technical Paper & Programmatic Recommendations
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the main human settlements,
    codified with the ICA Category of the relative province, used in the Integrated
    Context Analysis (ICA) run in Malawi in 2014. Data source: Global Discovery, 2007.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2da89aa8b2cc4bf496aa959958a051e6/data
  format: null
  id: resource_c79e0ae6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - Human Settlements, 2007
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the predominant livelihood zones
    - by district level - identified during the Integrated Context Analysis (ICA)
    run in Malawi in 2014. Data source: Malawi Vulnerability Assessment Committee
    (MVAC), 2009.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f0403bbc98054016bef1fbf69eeafdb6/data
  format: null
  id: resource_55ed1471
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - Predominant Livelihood Zones, 2009
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains the second-level administrative unit boundaries
    (districts) for Malawi. Data source: WFP'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c3795d2833e744e89fd1baec588a653a/data
  format: null
  id: resource_996e530f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - Second-level Administrative Boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the estimated numbers of food
    insecure people used in the Integrated Context Analysis (ICA) run in Malawi in
    2014. Data source: Malawi Vulnerability Assessment Committee (MVAC) & Household
    Economic Analysis (HEA), 2009-2013. The key indicators used for the analysis were
    the food insecure population figures and percentages.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/09d064e0001d4b7d86c153251b9617bd/data
  format: null
  id: resource_d7c32f48
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - Estimated Numbers of Food Insecure People, 2009-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the drought risk estimated during
    the Integrated Context Analysis (ICA) run in Malawi in 2014. Data source: Ministry
    of Finance and Economic Planning and Development, 2004-2013. The key indicator
    used for the analysis was the number of occurrences, triangulated with a 19-years
    and 5-years rainfall trend analysis to better understand the recent and long-term
    exposure to droughts.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/df4e45f9bced405cb5bc7f2972cb5a8c/data
  format: null
  id: resource_ae7bea87
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - Drought Risk, 2004-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the flood risk estimated during
    the Integrated Context Analysis (ICA) run in Malawi in 2014. Data source: Department
    of Disasters Management Affairs (DoDMA) 2000-2013, VAM - MEPED. The key indicator
    used for the analysis was the historical number of flood events.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/19a761ecc6c3431ea213e08a48484ecf/data
  format: null
  id: resource_abd1e804
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - Flood Risk, 2000-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the combined natural shocks
    risk (floods and droughts) estimated during the Integrated Context Analysis (ICA)
    run in Malawi in 2014. Data source: Department of Disaster Management Affairs
    (DoDMA) 2000-2013, VAM - MEPED, Ministry of Finance and Economic Planning and
    Development 2004-2013.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/e3b4c690269a4c1ca5d3796305ed723a/data
  format: null
  id: resource_4fbd2f05
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - Natural Shocks Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains the first-level administrative unit boundaries
    (provinces) for Malawi. Data source: WFP'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/812ca307d099433ca1d9090baa98514f/data
  format: null
  id: resource_aa823c99
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - First-level Administrative Boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the recurrence of food insecurity
    observed during the Integrated Context Analysis (ICA) run in Malawi in 2014. Data
    source: Comprehensive Food Security and Vulnerability Analysis (CFSVA) 2009, Integrated
    Household Survey (IHS) 2010-2011, urban and rural Emergency Food Security Assessment
    (EFSA) 2012-2013. The key indicator used for the analysis was the recurrence of
    Food Consumption Score (FCS) over the 30% threshold.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/93fbc2b3e88b45419f7fa2607e8f7445/data
  format: null
  id: resource_ac64ee12
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - Recurrence of Food Insecurity, 2009-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This Excel file contains the food security analysis performed for the
    purposes of the Integrated Context Analysis (ICA) run in Malawi in 2014. The analysis,
    using the Comprehensive Food Security Vulnerability Analysis (CFSVA) data and
    the Emergency Food Security Assessment (EFSA) data from 2009 to 2013, determines
    the recurrence of food insecurity conditions - by second-level administrative
    area - applying a threshold equal to 30%.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/9fefb7c6424a4a70bfe77600c5b92318/data
  format: null
  id: resource_8e2af240
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Malawi, 2014 - Food Insecurity Recurrence Analysis
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-mwi_wfp_integratedcontextanalysis_2014
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
  end: '2014-12-31'
  start: '2014-01-01'
temporal_resolution: null
title: 'Malawi: Integrated Context Analysis (ICA), 2014'
version: null
vulnerability: null
---

---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNISDR GAR 2015 Global Risk Assessment
    url: https://data.humdata.org/dataset/multi-hazard-average-annual-loss
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/multi-hazard-average-annual-loss
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/multi-hazard-average-annual-loss
dataset_id: rdls_lss-undrr_multihazardaverageannuall_20150101
description: 'GAR 2015 Risk results are presented as a series of probabilistic risk
  metrics. One of them is the multi-hazard Average Annual Loss (AAL) which is the
  long-term expected loss per year, averaged over many years. While there may actually
  be little or no losses, over a short period of time, the AAL accounts much larger
  losses that may occur more infrequently. AAL is also an indication of the amount
  of savings a nation need to set aside each year to cover the cost of long term losses
  from that hazard. As GAR global risk assessment is performed at global scale, the
  AAL calculated should be read as order of magnitude for the potential recurrent
  extent of losses in a country.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/multi-hazard-average-annual-loss]'
details: This dataset was generated using other global datasets; it should not be
  used for local applications (such as land use planning). The main purpose of GAR
  2015 datasets is to broadly identify high risk areas at global level and for identification
  of areas where more detailed data should be collected. Some areas may be underestimated
  or overestimated. Given this analysis was conducted using global datasets, the resolution
  of which is not sufficient for in-situ planning, it should not be used for critical
  (like life saving) decisions. UNISDR and collaborators should in no case be liable
  for misuse or misinterpretation of the presented results. The designations employed
  and the presentation of material on the maps do not imply the expression of any
  opinion whatsoever on the part of UNISDR or the Secretariat of the United Nations
  concerning the legal status of any country, territory, city or area or of its authorities,
  or concerning the delimitation of its frontiers or boundaries. The designations
  employed and the presentation of material on the maps do not imply the expression
  of any opinion whatsoever on the part of UNISDR or the Secretariat of the United
  Nations concerning the legal status of any country, territory, city or area or of
  its authorities, or concerning the delimitation of its frontiers or boundaries.
  This analysis was conducted using global datasets, the resolution of which is not
  relevant for in-situ planning and should not be used for life and death decisions.
  UNISDR and collaborators should in no case be liable for misuse of the presented
  results.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: GAR 2015 probabilistic risk assessment methodology integrates hazard,
    exposure, and vulnerability datasets at global scale to calculate multi-hazard
    average annual loss (AAL) per country. AAL represents the long-term expected economic
    loss per year, accounting for both frequent low-impact and infrequent high-impact
    events across five hazard types.
  sources:
  - id: source_1
    license: null
    name: UNISDR GAR 2015 Global Risk Assessment
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/multi-hazard-average-annual-loss
  rel: source
loss:
  losses:
  - asset_category: economic_indicator
    asset_dimension: index
    description: Multi-hazard average annual loss from earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Multi-hazard average annual loss from cyclone wind
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Multi-hazard average annual loss from storm surge
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Multi-hazard average annual loss from tsunami
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: null
      trigger: null
      type: tsunami
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Multi-hazard average annual loss from floods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: observed
        type: total
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
  description: Multi-hazard Average Annual Loss (Zipped shapefiles of multi-hazard
    average annual loss (17,903 kb).)
  download_url: https://data.humdata.org/dataset/a3b57464-fa02-49c3-a8a0-3f26e12a7ebf/resource/3d22ff81-7d26-4729-84aa-d4fe692bdc7d/download/gar2015.zip
  format: null
  id: resource_3d22ff81
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gar2015.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Multi-hazard Average Annual Loss (Excel files of multi-hazard average
    annual loss by country (978 kb).)
  download_url: https://data.humdata.org/dataset/a3b57464-fa02-49c3-a8a0-3f26e12a7ebf/resource/0c6bfc50-9f85-45c4-91a9-e43b38daad01/download/gar15-results.xlsm
  format: null
  id: resource_0c6bfc50
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GAR15 results.xlsm
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-undrr_multihazardaverageannuall_20150101
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-01-01'
temporal_resolution: null
title: Multi-hazard Average Annual Loss
version: null
vulnerability: null
---

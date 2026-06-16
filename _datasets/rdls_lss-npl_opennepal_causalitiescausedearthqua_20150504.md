---
attributions:
- entity:
    affiliation: null
    email: null
    name: Nepal Disaster Risk Reduction portal
    url: https://data.humdata.org/dataset/causalities-caused-by-earthquake-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/causalities-caused-by-earthquake-2015
creator:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/causalities-caused-by-earthquake-2015
dataset_id: rdls_lss-npl_opennepal_causalitiescausedearthqua_20150504
description: 'This dataset contains causualities such as death,injury,displaced population
  and other damages caused by earthquake, 2015. This dataset was extracted from Nepal
  Disaster Risk Reduction portal. Link: http://drrportal.gov.np/. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/causalities-caused-by-earthquake-2015]'
details: null
exposure: []
hazard: null
license: ODbL-1.0/
lineage:
  description: Post-event impact data extracted from the Nepal Disaster Risk Reduction
    portal documenting direct casualties (deaths, injuries), displacement, and damages
    caused by the 2015 earthquake. The dataset aggregates observed impact records
    from the official national disaster risk reduction information system.
  sources:
  - id: source_1
    license: null
    name: Nepal Disaster Risk Reduction portal
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/causalities-caused-by-earthquake-2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct fatalities from the 2015 earthquake in Nepal
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
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Direct injuries from the 2015 earthquake in Nepal
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displaced by the 2015 earthquake in Nepal
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage caused by the 2015 earthquake in Nepal
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: Nepal - Causalities caused by earthquake,2015 (CSV)
  download_url: http://data.opennepal.net/sites/all/modules/pubdlcnt/pubdlcnt.php?file=http://data.opennepal.net/sites/default/files/resources/clipboard_0.csv&nid=5362
  format: null
  id: resource_12f2a269
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: clipboard_0.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_opennepal_causalitiescausedearthqua_20150504
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-05-04'
temporal_resolution: null
title: Nepal - Causalities caused by earthquake,2015
version: null
vulnerability: null
---

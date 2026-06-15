---
attributions:
- entity:
    affiliation: null
    email: null
    name: Ministry of Home and Affairs Nepal Disaster Report 2013
    url: https://data.humdata.org/dataset/estimated-loss-during-disaster-in-2012-and-2013
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/estimated-loss-during-disaster-in-2012-and-2013
creator:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/estimated-loss-during-disaster-in-2012-and-2013
dataset_id: rdls_lss-npl_opennepal_estimatedlossduringdisast_20140509
description: 'This data set include impact of disaster i.e estimated loss due to disaster
  in 2012-13. It was extracted from Nepal disaster Report 2013 which was published
  by Ministry of Home and Affair. Link : http://www.moha.gov.np//uploads/publications/file/Nepal%20Disaster%20Rep....
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/estimated-loss-during-disaster-in-2012-and-2013]'
details: null
exposure: []
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Post-event disaster impact data compiled by Nepal's Ministry of Home
    and Affairs from official disaster reports covering 2012-2013. Economic losses
    were estimated and aggregated by hazard type and geographic area to produce the
    national disaster report.
  sources:
  - id: source_1
    license: null
    name: Ministry of Home and Affairs Nepal Disaster Report 2013
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/estimated-loss-during-disaster-in-2012-and-2013
  rel: source
loss:
  losses:
  - asset_category: economic_indicator
    asset_dimension: index
    description: Direct economic losses from flooding during 2012-2013 disasters in
      Nepal
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
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Direct economic losses from earthquakes during 2012-2013 disasters
      in Nepal
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
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Direct economic losses from landslides during 2012-2013 disasters
      in Nepal
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
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
  description: Nepal - Estimated loss during disaster in 2012 and 2013 (Datasets%20for%20OpenNepal%20-%2031.csv)
  download_url: http://data.opennepal.net/sites/all/modules/pubdlcnt/pubdlcnt.php?file=http://data.opennepal.net/sites/default/files/resources/Datasets%20for%20OpenNepal%20-%2031.csv&nid=2546
  format: null
  id: resource_37b6a400
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Datasets%20for%20OpenNepal%20-%2031.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_opennepal_estimatedlossduringdisast_20140509
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
  start: '2014-05-09'
temporal_resolution: null
title: Nepal - Estimated loss during disaster in 2012 and 2013
version: null
vulnerability: null
---

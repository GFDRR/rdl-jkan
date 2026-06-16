---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/dtm-dominica-preliminary-report-on-schools-used-as-shelter
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/dtm-dominica-preliminary-report-on-schools-used-as-shelter
dataset_id: rdls_el-dma_iom_dtmdominicapreliminaryrep_20171014
description: 'The Ministry of Education announced the first phase of school reopening
  on 16 October 2017. Therefore, IOM prioritized schools currently housing the displaced
  population in the first round of DTM assessment. 43 of the pre-identified collective
  centers were schools and 33 of these were housing displaced individuals on 6 October.
  IOM aims to provide basic information on these targeted schools to inform the government
  and general humanitarian community of the situation in these collective centers
  and support provision of assistance. This report presents the results of assessments
  carried out from 11-14 October in 19 schools that are scheduled to reopen in the
  coming days.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/dtm-dominica-preliminary-report-on-schools-used-as-shelter]'
details: null
exposure:
- asset_type:
    description: School buildings identified and assessed as collective shelter centers
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM conducted rapid assessments of 43 pre-identified schools functioning
    as collective centers in Dominica following the 2017 earthquake disaster. Field
    teams documented shelter locations, capacity, and displaced population counts
    on 6 October 2017 to inform government and humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/dtm-dominica-preliminary-report-on-schools-used-as-shelter
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Displaced population housed in school shelters following earthquake
      disaster
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
        metric: displaced
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM Dominica, Preliminary Report on Schools used as Shelter (Prioritized
    schools being used as shelter after Hurricane Maria)
  download_url: https://data.humdata.org/dataset/5bccfa45-b905-4279-bb46-0070e5553a14/resource/461291ad-50d0-4710-a0ab-0ddf2b6af062/download/schools-shelters.kmz
  format: null
  id: resource_461291ad
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Schools-Shelters.kmz
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-dma_iom_dtmdominicapreliminaryrep_20171014
spatial:
  bbox: null
  centroid: null
  countries:
  - DMA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-10-14'
temporal_resolution: null
title: DTM Dominica, Preliminary Report on Schools used as Shelter
version: null
vulnerability: null
---

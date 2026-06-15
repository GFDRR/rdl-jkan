---
attributions:
- entity:
    affiliation: null
    email: null
    name: Inter Cluster IM Group partners on ground
    url: https://data.humdata.org/dataset/internally-displaced-population
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA South Sudan
  url: https://data.humdata.org/dataset/internally-displaced-population
creator:
  affiliation: null
  email: null
  name: OCHA South Sudan
  url: https://data.humdata.org/dataset/internally-displaced-population
dataset_id: rdls_lss-ssd_ochassd_internallydisplacedpopula_2013
description: 'The aim of the Displaced count monitor is to keep the Inter Cluster
  IM Group abreast with the movement of the displaced population and their returns.
  The data is the best availableat the moment. The IDP/Returnee figures are based
  on reports from partners on ground. Majority of them have not been verified. Verification
  of the figures is a work in progress. The field named ''Count Verification status''
  gives information on the status of verification for each location. 1. Verified -
  Actual counting done by partners 2. Assessed but unverified - Location visited and
  figure estimated by a partner figure. No counting done. 3. Reported but unverified
  - Reported by South Sudan Relief and Rehabilitation Commission (SSRRC) and similar
  partners but no assessment or counting done. The data can also be improved with
  better accuracy of site coordinates. Kindly share any coordinates you might have
  from the field and help the ICIMG improve the dataset. The Site ID is an arbitrary
  unique number given to a location identified to have IDPs. The numbers are assigned
  randomly starting from 1. The site ID does not change and can only be used once.
  If a site is closed or if all people move from the site, the number is not reassigned
  to another site. To present a better picture of the locational settings of those
  displaced, IOM is supporting OCHA to categorize the locations as in the field named
  ''Type of location''. So far, the categories are 1. IDPs in UNMISS PoC area 2. IDPs
  Spontaneous settlement 3. IDPs Collective center 4. IDPs Integrated with host community
  5. IDPs Location not categorised 6. Crisis-displaced returns 7. IDPs Integrated
  with host community + Crisis-displaced returns 8. IDPs Location not categorised
  + Crisis-displaced returns 9. Affected host community 10. IDPs Spontaneous settlement
  + Affected host community 11. IDPs Location not categorised + Affected host community
  12. No caseload at the moment. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/internally-displaced-population]'
details: The IDP/Returns/Affected Host community figures are based on reports from
  partners on ground. Majority of them have not been verified. Verification of the
  figures is a work in progress.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Internally displaced population counts compiled from direct observational
    reports submitted by humanitarian partners operating in South Sudan. Data represents
    both verified counts from actual partner enumerations and assessed but unverified
    estimates from location visits, with verification status tracked for each geographic
    location.
  sources:
  - id: source_1
    license: null
    name: Inter Cluster IM Group partners on ground
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/internally-displaced-population
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced population counts and returnee figures from
      conflict-related displacement
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
          quantity_kind: count
          unit: null
        metric: displaced
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan - Internally Displaced Population (South Sudan Crisis -
    Displaced Count Monitor (30Jan2015).xlsx)
  download_url: https://data.humdata.org/dataset/a9a1cea3-28c7-472e-a888-a3f6f7970c4d/resource/08746071-6f1d-40ca-b2d4-1d1c84e48a6b/download/south-sudan-crisis-displaced-count-monitor-30jan2015.xlsx
  format: null
  id: resource_08746071
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: South Sudan Crisis - Displaced Count Monitor (30Jan2015).xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ssd_ochassd_internallydisplacedpopula_2013
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
  end: '2015-01-30'
  start: '2013-12-23'
temporal_resolution: null
title: South Sudan - Internally Displaced Population
version: null
vulnerability: null
---

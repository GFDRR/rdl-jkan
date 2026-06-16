---
attributions:
- entity:
    affiliation: null
    email: null
    name: International bilateral and multilateral organizations
    url: https://data.humdata.org/dataset/financial-aid-data-for-earthquake-as-of-june-92015
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NGOs and INGOs
    url: https://data.humdata.org/dataset/financial-aid-data-for-earthquake-as-of-june-92015
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Corporate and organizational donors
    url: https://data.humdata.org/dataset/financial-aid-data-for-earthquake-as-of-june-92015
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Informal communities and individuals
    url: https://data.humdata.org/dataset/financial-aid-data-for-earthquake-as-of-june-92015
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/financial-aid-data-for-earthquake-as-of-june-92015
creator:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/financial-aid-data-for-earthquake-as-of-june-92015
dataset_id: rdls_lss-npl_opennepal_financialaiddataearthquak_20150506
description: 'This dataset accumulates all foreign and national aid: Relief and rehabilitation
  aid coming from various International bilateral and multilateral organizations (including
  country governments)Relief and rehabilitation aid from NGOs and INGOs operating
  within and outside the countryRelief and rehabilitation aid from different corporates
  and organizations operating within and outside Nepal.Relief and rehabilitation aid
  from informal communities and individualsRelief and rehabilitation aid being given
  to national governments, local governments or spent directly by donors and intermediary
  organizationsRelief and rehabilitation aid in terms of both cash and in-kind supportRelief
  and rehabilitation aid accumulated in Prime Minister Relief Fund. Sources : http://fts.unocha.org/pageloader.aspx?page=emerg-emergencyDetails&appeal...
  http://www.uschamberfoundation.org/corporate-citizenship-center/nepal-ea... http://www.onlinekhabar.com/
  http://en.wikipedia.org/wiki/2015_Nepal_earthquake. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/financial-aid-data-for-earthquake-as-of-june-92015]'
details: null
exposure: []
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: This dataset aggregates financial aid and relief funding mobilized
    in response to the 2015 Nepal earthquake from multiple sources including bilateral/multilateral
    organizations, NGOs/INGOs, corporate entities, and informal donors. The data represents
    cumulative relief and rehabilitation aid flows as of June 9, 2015, compiled by
    OpenNepal from various contributing organizations and intermediaries.
  sources:
  - id: source_1
    license: null
    name: International bilateral and multilateral organizations
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: NGOs and INGOs
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Corporate and organizational donors
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: Informal communities and individuals
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/financial-aid-data-for-earthquake-as-of-june-92015
  rel: source
loss:
  losses:
  - asset_category: economic_indicator
    asset_dimension: index
    description: Financial aid and relief funding mobilized in response to the 2015
      Nepal earthquake
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
  description: Nepal - Financial Aid data for earthquake as of June 9,2015 (CSV)
  download_url: http://data.opennepal.net/sites/all/modules/pubdlcnt/pubdlcnt.php?file=http://data.opennepal.net/sites/default/files/resources/June-9-data.csv&nid=5363
  format: null
  id: resource_03de7f3c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June-9-data.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_opennepal_financialaiddataearthquak_20150506
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
  start: '2015-05-06'
temporal_resolution: null
title: Nepal - Financial Aid data for earthquake as of June 9,2015
version: null
vulnerability: null
---

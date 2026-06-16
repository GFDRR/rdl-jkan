---
attributions:
- entity:
    affiliation: null
    email: null
    name: Multiple Indicator Cluster Surveys (MICS)
    url: https://data.humdata.org/dataset/unicef-mg-new-internal-disp
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Demographic and Health Surveys (DHS)
    url: https://data.humdata.org/dataset/unicef-mg-new-internal-disp
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: United Nations organizations administrative sources
    url: https://data.humdata.org/dataset/unicef-mg-new-internal-disp
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNICEF Data and Analytics (HQ)
  url: https://data.humdata.org/dataset/unicef-mg-new-internal-disp
creator:
  affiliation: null
  email: null
  name: UNICEF Data and Analytics (HQ)
  url: https://data.humdata.org/dataset/unicef-mg-new-internal-disp
dataset_id: rdls_lss-unicef_newinternaldisplacements_2008
description: 'New internal displacements. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unicef-mg-new-internal-disp]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Displacement indicator data compiled from inter-agency estimates and
    nationally representative household surveys (MICS, DHS) supplemented with administrative
    records from UN organizations. Data aggregated to produce global estimates of
    new internal displacements, with disaggregation by demographic groups (children,
    men) and contextual factors (COVID-19, migration).
  sources:
  - id: source_1
    license: null
    name: Multiple Indicator Cluster Surveys (MICS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Demographic and Health Surveys (DHS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: United Nations organizations administrative sources
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unicef-mg-new-internal-disp
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internal displacement counts attributed to drought and climate-related
      stressors
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
purpose: Please consult (see referenced_by) or email data@unicef.org
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://data.unicef.org
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New internal displacements (.MG_NEW_INTERNAL_DISP..?format=csv)
  download_url: https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,MG,1.0/.MG_NEW_INTERNAL_DISP..?format=csv
  format: null
  id: resource_7a32b853
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: New internal displacements (CSV)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New internal displacements
  download_url: https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,MG,1.0/.MG_NEW_INTERNAL_DISP..
  format: null
  id: resource_4f89eb8f
  media_type: application/xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: New internal displacements (XML)
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-unicef_newinternaldisplacements_2008
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
  end: '2023-12-31'
  start: '2008-01-01'
temporal_resolution: null
title: New internal displacements
version: null
vulnerability: null
---

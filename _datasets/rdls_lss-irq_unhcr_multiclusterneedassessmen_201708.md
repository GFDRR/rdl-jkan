---
attributions:
- entity:
    affiliation: null
    email: null
    name: REACH
    url: https://data.humdata.org/dataset/unhcr-irq-2018-mcna-v2-1
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Iraq Assessment Working Group
    url: https://data.humdata.org/dataset/unhcr-irq-2018-mcna-v2-1
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-irq-2018-mcna-v2-1
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-irq-2018-mcna-v2-1
dataset_id: rdls_lss-irq_unhcr_multiclusterneedassessmen_201708
description: 'The Multi Cluster Needs Assessment (MCNA) is an iterative cluster-led
  program and the primary multi-cluster nationwide needs assessment in Iraq. It provides
  a quantitative evidence base for humanitarian decision makers with the purpose of
  informing planning, sector prioritization and target group identification. The MCNA
  seeks to understand multi-sectoral household conditions and priority needs of conflict-affected
  populations living in Iraq and to provide insights that allow aid sectors to understand
  geographic differences in humanitarian conditions and needs, as well as to identify
  gaps and opportunities for the provision of humanitarian assistance across Iraq.
  The MCNA allows for in-depth nation-wide analysis, enabling the identification of
  mid to long-term trends and shifting needs over time. The findings from this assessment
  provide a comprehensive overview of multi-sectoral household needs and priorities
  to inform the humanitarian response and strategic programming in Iraq.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-irq-2018-mcna-v2-1]'
details: The data must be requested via the resource download link
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Household-level needs data collected via computer-assisted personal
    interviews (CAPI) by REACH under the Iraq Assessment Working Group framework.
    Data aggregated across multiple humanitarian sectors (education, food security,
    health, livelihoods, protection, shelter) to provide multi-sectoral needs profiles
    for conflict-affected populations, enabling geographic prioritization and sector-specific
    targeting.
  sources:
  - id: source_1
    license: null
    name: REACH
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Iraq Assessment Working Group
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unhcr-irq-2018-mcna-v2-1
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multi-sectoral humanitarian needs of conflict-affected households
      in Iraq
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
        metric: exposure
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
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/909/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_d15d6fe9
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Iraq - Iraq Multi Cluster Need Assessment, 2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Iraq Multi Cluster Need Assessment, 2018 (Contains information
    about the dataset's metadata and data)
  download_url: https://microdata.unhcr.org/index.php/catalog/909/pdf-documentation
  format: null
  id: resource_a74d5b81
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Codebook
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-irq_unhcr_multiclusterneedassessmen_201708
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-08-31'
  start: '2017-08-09'
temporal_resolution: null
title: Iraq - Iraq Multi Cluster Need Assessment, 2018
version: null
vulnerability: null
---

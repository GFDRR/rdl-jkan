---
attributions:
- entity:
    affiliation: null
    email: null
    name: Multiple peer-reviewed hazard, exposure, and vulnerability datasets
    url: https://data.humdata.org/dataset/worldriskindex
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Social, economic, and political indicators
    url: https://data.humdata.org/dataset/worldriskindex
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Institute for International Law of Peace and Armed Conflict
  url: https://data.humdata.org/dataset/worldriskindex
creator:
  affiliation: null
  email: null
  name: Institute for International Law of Peace and Armed Conflict
  url: https://data.humdata.org/dataset/worldriskindex
dataset_id: rdls_el-ifhv_worldriskindex_2000
description: "The WorldRiskIndex is a statistical model that provides an assessment\
  \ of the latent risk of 193 countries falling victim to a humanitarian disaster\
  \ caused by extreme natural events and the negative impacts of climate change. Based\
  \ on peer-reviewed concepts of risk, hazard and vulnerability, it is assumed that\
  \ disaster risks are not solely shaped by the occurrence, intensity, and duration\
  \ of extreme natural events, but that social factors, political conditions, and\
  \ economic structures are equally responsible for whether disasters occur in the\
  \ context of extreme natural events. Accordingly, both main spheres of disaster\
  \ risk, exposure and vulnerability, are treated as equals. The WorldRiskIndex was\
  \ initially developed in 2011 by the United Nations University Institute for Environment\
  \ and Human Security (UNU-EHS) for B\xC3\xBCndnis Entwicklung Hilft as a model with\
  \ 27 indicators to analytically link and relate the two spheres of disaster risks\
  \ - exposure to natural hazards such as earthquakes, storms or droughts, and societal\
  \ capacities to respond to these kinds of events. The methodology of the WorldRiskIndex\
  \ has been continuously revised and developed by the Institute for International\
  \ Law of Peace and Armed Conflict (IFHV) since 2018. In 2022, a new, fully revised\
  \ model of the WorldRiskIndex was published, enabling more accurate analyses by\
  \ incorporating more than 100 high-quality indicators, new data sources, and more\
  \ robust statistical methods, thus finally replacing the previously used model..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldriskindex]"
details: The new WorldRiskIndex focuses on the latent risk of disasters due to extreme
  natural events and adverse impacts of climate change. Other types of risk such as
  conflicts, wars, or pandemics are deliberately only partially or not at all considered,
  as the driving forces of these risks differ in many respects from those of risks
  from natural events and climate. Furthermore, it would be extremely difficult and,
  in many cases, impossible to integrate their explanatory approaches into the new
  model's concepts, structures, and processes. A transfer of the WorldRiskIndex results
  to these areas is therefore not possible, or only possible to a limited degree.
  In addition, some vulnerability categories, such as infrastructure, social networks,
  or material security, could not be included in the calculation despite their practical
  relevance due to a lack of data availability. As part of continuous revisions and
  updates, these gaps are to be filled using new methods or geospatial analysis. However,
  the new structure of the WorldRiskIndex already allows users to use their data in
  combination with the results provided to fill 'white spots' in the model and to
  realize specific analyses.
exposure:
- asset_type:
    description: National population exposed to extreme natural events and climate
      change impacts
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
    description: Economic structures and development indicators affecting vulnerability
      to disasters
    id: economic_indicator
    scheme: null
    title: null
    uri: null
  category: economic_indicator
  id: exposure_2
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: currency
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: The WorldRiskIndex integrates peer-reviewed hazard exposure data (extreme
    natural events and climate change impacts) with national-level social, economic,
    and political vulnerability indicators through a statistical model to produce
    a composite risk index for 193 countries. The model assumes disaster risk emerges
    from the interaction of hazard occurrence/intensity with underlying social and
    economic structures, generating a latent risk assessment rather than post-event
    impact data.
  sources:
  - id: source_1
    license: null
    name: Multiple peer-reviewed hazard, exposure, and vulnerability datasets
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Social, economic, and political indicators
    risk_data_type:
    - vulnerability
    type: dataset
    url: null
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/worldriskindex
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Latent risk of humanitarian disaster from extreme natural events
      affecting national populations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: null
      trigger: null
      type: extreme_temperature
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://weltrisikobericht.de/en/
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://www.ifhv.de/
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://www.ifhv.de/publications/world-risk-report
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Additional information on the structure, calculation and indicators
    of the WorldRiskIndex datasets and geopackages.
  download_url: https://data.humdata.org/dataset/1efb6ee7-051a-440f-a2cf-e652fecccf73/resource/6aca2f09-ab01-4ff7-a17d-8cac9686cbba/download/worldriskindex-meta.xlsx
  format: null
  id: resource_6aca2f09
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: worldriskindex-meta.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A longitudinal dataset for long-term trend analysis; data as of September
    24, 2025; annual updates and revisions - see metadata for more information.
  download_url: https://data.humdata.org/dataset/1efb6ee7-051a-440f-a2cf-e652fecccf73/resource/3a2320fa-41b4-4dda-a847-3f397d865378/download/worldriskindex-trend.csv
  format: null
  id: resource_3a2320fa
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: worldriskindex-trend.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A longitudinal geopackages for long-term trend analysis; data as of
    September 24, 2025; annual updates and revisions - see metadata for more information.
  download_url: https://data.humdata.org/dataset/1efb6ee7-051a-440f-a2cf-e652fecccf73/resource/360962d8-ddc6-49e6-a932-127f9b445565/download/worldriskindex-trend.gpkg
  format: null
  id: resource_360962d8
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: worldriskindex-trend.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: An archive of stand-alone datasets from the annual WorldRiskReport
    based on the new methodology published in 2022; all data as of September 09, 2024;
    annual additions planned; all datasets correspond to values published in the respective
    years of the WorldRiskReport; to analyze long-term trends, please use the longitudinal
    data provided - see metadata for more details.
  download_url: https://data.humdata.org/dataset/1efb6ee7-051a-440f-a2cf-e652fecccf73/resource/9dd7ca94-94fe-473a-9f53-277bf6544df1/download/worldriskindex-datasets.zip
  format: null
  id: resource_9dd7ca94
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: worldriskindex-datasets.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: An archive of stand-alone geopackages from the annual WorldRiskReport
    based on the new methodology published in 2022; all data as of September 24, 2025;
    annual additions planned; all geopackages correspond to values published in the
    respective years of the WorldRiskReport; to analyze long-term trends, please use
    the longitudinal data provided - see metadata for more details.
  download_url: https://data.humdata.org/dataset/1efb6ee7-051a-440f-a2cf-e652fecccf73/resource/09a641cd-d07f-4de9-8cf6-b0fbaa48ff21/download/worldriskindex-geopackages.zip
  format: null
  id: resource_09a641cd
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: worldriskindex-geopackages.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A special analysis of global conflict exposure based on the ACLED Conflict
    Exposure Dataset for the years 2020 to 2023 as published in the WorldRiskreport
    2024.
  download_url: https://data.humdata.org/dataset/1efb6ee7-051a-440f-a2cf-e652fecccf73/resource/b9f8b354-675c-471d-aa17-11a2689823cd/download/special-issue-conflict-exposure.xlsx
  format: null
  id: resource_b9f8b354
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Special Issue Conflict Exposure.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: An archive for the historical model and supplementary materials of
    the WorldRiskIndex for the WorldRiskReports from 2011 to 2021 - this archive is
    only provided as supplementary material for the mentioned reports and is no longer
    maintained or updated.
  download_url: https://data.humdata.org/dataset/1efb6ee7-051a-440f-a2cf-e652fecccf73/resource/a00f93fa-a159-4868-9ce0-7d90f58e3d20/download/worldriskindex-legacy.zip
  format: null
  id: resource_a00f93fa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WorldRiskIndex Legacy Archive.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ifhv_worldriskindex_2000
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
  end: '2025-09-24'
  start: '2000-01-01'
temporal_resolution: null
title: WorldRiskIndex
version: null
vulnerability: null
---

---
attributions:
- entity:
    affiliation: null
    email: null
    name: Flowminder
    url: https://data.humdata.org/dataset/mobility-patterns-west-africa
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/mobility-patterns-west-africa
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Flowminder (inactive)
  url: https://data.humdata.org/dataset/mobility-patterns-west-africa
creator:
  affiliation: null
  email: null
  name: Flowminder (inactive)
  url: https://data.humdata.org/dataset/mobility-patterns-west-africa
dataset_id: rdls_exp-flowminder_mobilitypatternspopulatio_2013
description: 'Here we provide version 1 Flowminder (www.flowminder.org) human mobility
  models for West Africa, together with WorldPop population density data for the region,
  to support ongoing efforts to control the ebola outbreak. Before downloading any
  data, please read the documention carefully as it provides details on the datasets
  and models provided through the links below. The mobility data refer to estimated
  patterns before the Ebola outbreak and should be interpreted with caution for Ebola
  affected countries as mobility patters are known to have changed. Additional discussion
  by the authors around the use of mobile operator data for epidemilogical research
  see: http://currents.plos.org/outbreaks/article/containing-the-ebola-outbreak-the-potential-and-challenge-of-mobile-network-data/.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mobility-patterns-west-africa]'
details: The mobility data refer to estimated patterns before the Ebola outbreak and
  should be interpreted with caution for Ebola affected countries as mobility patters
  are known to have changed. Please see the detailed documentation provided.
exposure:
- asset_type:
    description: High-resolution gridded population density at 100x100m resolution
      for West Africa, 2014
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
      quantity_kind: area
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: WorldPop population density data were generated from census records
    and satellite-derived settlement maps at 100x100m resolution. Flowminder mobility
    models were developed from mobile phone call detail records and statistical inference
    to estimate human movement patterns. Both datasets were compiled for West Africa
    to support disease outbreak response planning, with mobility patterns representing
    pre-outbreak baseline conditions.
  sources:
  - id: source_1
    license: null
    name: Flowminder
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mobility-patterns-west-africa
  rel: source
loss: null
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
  url: http://www.worldpop.org.uk/ebola/Flowminder-Mobility-Data-21.08.14.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Documentation: http://www.worldpop.org.uk/ebola/Flowminder-Mobility-Data-21.08.14.pdf
    Spatial data files: http://www.worldpop.org.uk/ebola/Spatial_Data.7z'
  download_url: http://www.worldpop.org.uk/ebola/mobility_data/mobility-data-1stSept14.zip
  format: null
  id: resource_d9899ae6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Estimated mobility patterns for West Africa
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The data show newly created WorldPop datasets of estimated population
    counts per 100m x 100m grid cell for West African countries, adjusted to match
    the latest UN estimates for 2014. The WorldPop methods page (http://www.worldpop.org.uk/data/methods/)
    provides information on the approaches and input datasets used to construct the
    estimates.
  download_url: http://www.worldpop.org.uk/ebola/
  format: null
  id: resource_3d39aa14
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Estimated high resolution population densities for West Africa (100x100m),
    2014
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-flowminder_mobilitypatternspopulatio_2013
spatial:
  bbox: null
  centroid: null
  countries:
  - BEN
  - BFA
  - CIV
  - GHA
  - GIN
  - GMB
  - GNB
  - LBR
  - MLI
  - MRT
  - NER
  - SEN
  - SLE
  - TGO
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2014-04-01'
  start: '2013-01-01'
temporal_resolution: null
title: Mobility patterns and population densities for West Africa
version: null
vulnerability: null
---

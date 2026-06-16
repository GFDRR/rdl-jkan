---
attributions:
- entity:
    affiliation: null
    email: null
    name: FAO
    url: https://data.humdata.org/dataset/wfp-and-fao-overview-of-countries-affected-by-the-2015-16-el-nino
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP
    url: https://data.humdata.org/dataset/wfp-and-fao-overview-of-countries-affected-by-the-2015-16-el-nino
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Global Food Security Cluster
    url: https://data.humdata.org/dataset/wfp-and-fao-overview-of-countries-affected-by-the-2015-16-el-nino
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/wfp-and-fao-overview-of-countries-affected-by-the-2015-16-el-nino
creator:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/wfp-and-fao-overview-of-countries-affected-by-the-2015-16-el-nino
dataset_id: rdls_hl-bolswztlsvnm_hdx_wfpfaooverviewcountriesaf_20160421
description: "This dataset contains a list of the countries affected by the El Ni\xF1\
  o as at April 21, 2016 as reported jointly by FAO, the Global Food Security Cluster\
  \ and WFP on 21 April 2016 in the 2015-2016 El Ni\xF1o: WFP and FAO Overview update.\
  \ According to the World Bank, El Ni\xF1o is likely to have a negative impact in\
  \ more isolated local food markets, and many countries are already facing increased\
  \ food prices. Food Security Cluster partners have implemented preparedness activities\
  \ and are responding in countries where the effects of El Ni\xF1o have materialised,\
  \ such as Ethiopia, Papua New Guinea, Malawi and throughout Central America. In\
  \ Southern Africa, many areas have seen the driest October-December period since\
  \ at least 1981, and some 14 million people in the region are already facing hunger,\
  \ which adds to fears of a spike in the numbers of the food insecure later this\
  \ year through 2017.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wfp-and-fao-overview-of-countries-affected-by-the-2015-16-el-nino]"
details: "The data was extracted from list of affected countries from the 2015-2016\
  \ El Ni\xF1o: WFP and FAO Overview update issued by the Global Food Security Cluster\
  \ on 21 April 2016 which can be downloaded from the GFSC website here: http://www.foodsecuritycluster.net/document/2015-2016-el-nino-wfp-and-fao-overview"
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Joint assessment by FAO, WFP, and Global Food Security Cluster of\
    \ countries affected by the 2015-2016 El Ni\xF1o event, compiled from direct observational\
    \ and anecdotal data on food security impacts, food price increases, and humanitarian\
    \ preparedness activities as of April 2016."
  sources:
  - id: source_1
    license: null
    name: FAO
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: WFP
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Global Food Security Cluster
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wfp-and-fao-overview-of-countries-affected-by-the-2015-16-el-nino
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: "Food security impacts and increased food prices in countries affected\
      \ by El Ni\xF1o-induced drought"
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
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
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
  description: WFP and FAO overview of countries affected by the El Nino.csv
  download_url: https://docs.google.com/spreadsheets/d/1OARCnErSnC0vGt7_BM3QgQ-i_KKb5inMum4fMNsOVrE/pub?gid=0&single=true&output=csv
  format: null
  id: resource_908f226a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WFP and FAO overview of countries affected by the El Nino.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "WFP and FAO Overview of Countries Affected by the El Ni\xF1o (GeoJSON)"
  download_url: https://data.humdata.org/dataset/2f804189-4228-4171-88ad-74273399af3c/resource/de96f6a5-9f1f-4702-842c-4082d807b1c1/download/fao-wfp-elnino-overview.geojson
  format: null
  id: resource_de96f6a5
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fao-wfp-elnino-overview.geojson
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-bolswztlsvnm_hdx_wfpfaooverviewcountriesaf_20160421
spatial:
  bbox: null
  centroid: null
  countries:
  - BOL
  - SWZ
  - TLS
  - VNM
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-04-21'
temporal_resolution: null
title: "WFP and FAO Overview of Countries Affected by the El Ni\xF1o"
version: null
vulnerability: null
---

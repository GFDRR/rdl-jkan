---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP HQ VAM Analysis of Chirps Rainfall Estimates (RFE)
    url: https://data.humdata.org/dataset/ica-sudan-2018-drought-risk-1982-2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/ica-sudan-2018-drought-risk-1982-2017
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/ica-sudan-2018-drought-risk-1982-2017
dataset_id: rdls_hzd-sdn_ochasdn_ica2018droughtrisk1982201_20181122
description: 'This layer contains information about the drought risk - by second-level
  administrative area - estimated during the Integrated Context Analysis (ICA) run
  in Sudan in 2018. Data source: HQ VAM Analysis of Chirps Rainfall Estimates (RFE),
  1982-2017. The main indicators used for the analysis were the number of poor growing
  seasons observed in the time window of interest and the inter-annual rainfall variability..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ica-sudan-2018-drought-risk-1982-2017]'
details: https://geonode.wfp.org/layers/geonode%3Asdn_ica_droughtrisk_geonode_20180201
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
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
  description: 'WFP VAM processed CHIRPS rainfall estimates (1982-2017) to calculate
    two key indicators: number of poor growing seasons and inter-annual rainfall variability.
    These indicators were aggregated by second-level administrative boundaries to
    produce a drought risk classification for the 2018 ICA Sudan analysis.'
  sources:
  - id: source_1
    license: null
    name: WFP HQ VAM Analysis of Chirps Rainfall Estimates (RFE)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ica-sudan-2018-drought-risk-1982-2017
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: https://geonode.wfp.org/geoserver/wfs?format_options=charset%3AUTF-8&typename=geonode%3Asdn_ica_droughtrisk_geonode_20180201&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'This layer contains information about the drought risk - by second-level
    administrative area - estimated during the Integrated Context Analysis (ICA) run
    in Sudan in 2018. Data source: HQ VAM Analysis of Chirps Rainfall Estimates (RFE),
    1982-2017. The main indicators used for the analysis were the number of poor growing
    seasons observed in the time window of interest and the inter-annual rainfall
    variability.'
  download_url: null
  format: null
  id: resource_0fbecdb0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Drought Risk, 1982-2017
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_ochasdn_ica2018droughtrisk1982201_20181122
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-11-22'
temporal_resolution: null
title: ICA Sudan, 2018 - Drought Risk, 1982-2017
version: null
vulnerability: null
---

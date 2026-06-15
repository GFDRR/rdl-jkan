---
attributions:
- entity:
    affiliation: null
    email: null
    name: INFORM Risk Framework
    url: https://data.humdata.org/dataset/inform-based-prioritization-of-enumeration-areas-in-malawi
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Malawi Spatial Data Platform (MASDAP)
    url: https://data.humdata.org/dataset/inform-based-prioritization-of-enumeration-areas-in-malawi
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/inform-based-prioritization-of-enumeration-areas-in-malawi
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/inform-based-prioritization-of-enumeration-areas-in-malawi
dataset_id: rdls_el-mwi_nlrc510_informbasedprioritization_20170714
description: 'A crude version of the INFORM risk-framework is applied to Enumeration
  Areas (which is unofficial, but is deeper than admin-3), in Southern Malawi. This
  is done specifically for area selection regarding the ECHO2 project in 3 TA''s:
  Mwambo (Zomba district), Makhwira (Chikwawa district) and Ndamera (Nsanje district).
  Scope Enumeration areas are retrieved from http://www.masdap.mw/layers/geonode%3Aeas_bnd.
  These are used, because we want to prioritize on a deeper level than Traditional
  Authority (admin-3) level, and there are no other official boundaries available.
  The dataset in principle data for the whole of Malawi, but contains 4 filters, which
  can be applied, which are the following: Filter_south: this filters out only the
  South of Malawi, for which the drough and flood analysis has been carried out (see
  details below). Filter_district: contains all EA''s from the 3 pre-identified districts
  Zomba, Chikwawa and Nsanje. Filter_TA: contains all EA''s from the 3 pre-identified
  TAs Mwambo, Makhwira and Ndamera. Filter_GVH: there are also 44 Group Village Heads
  pre-identified for the project. As these GVH''s are points on a map, all EA''s are
  selected here which have a GVH within their boundaries or very close to their boundaries.
  INFORM risk-framework The INFORM framework (http://www.inform-index.org/) is applied
  to assess risk per community, which is considered the main criteria for prioritization
  within the project. Because of low data availability we apply a crude version for
  now, with only some important indicators of the framework actually used. Since we
  feel that these indicators (see below) still constitute together a current good
  assessment of risk, and we want to stimulate the use and acceptance of the INFORM-framework,
  we choose to use it anyway. The INFORM risk-score consists of 3 main components:
  hazards, vulnerability and coping capacity. Hazard: For hazard we focus - in line
  with the ECHO2 project - on floods and droughts only. Analysis has been carried
  out (see more details below), to determine flood and drought risk on a scale from
  0-10 with a resolution of 250meter grid cells. This has subsequently been aggregated
  to Enumeration Areas, by taking a population-weighted average. Thereby taking into
  account where people actually live within the Enumeration Areas. (Population data
  source: Worldpop: http://www.worldpop.org.uk/data/summary/?doi=10.5258/SOTON/WP00155)
  Vulnerability: Vulnerability is operationalized here through poverty incidence.
  Poverty rate (living below $1.25/day) is retrieved from Worldpop (http://www.worldpop.org.uk/data/summary/?doi=10.5258/SOTON/WP00157)
  and again transformed from a 1km resolution grid to Enumeration Areas through a
  population-weighted average. Lack of Coping capacity: Coping capacity is measured
  through traveltimes to various facilities, namely traveltime to nearest hospistal,
  traveltime to nearest trading centre and traveltime to nearest secondary school.
  Together these are all proxies of being near/far to facilities, and thereby an indicator
  of having higher/lower coping capacity. See https://510.global/developing-and-field-testing-a-remoteness-indicator-in-malawi/
  for more information on how these traveltimes were calculated and validated. Use
  All features are stored in a CSV, but can easily be joined to the geographic shapefile
  to make maps on EACODE. Flood and Drought calculations Drought layer The drought
  risk map was created by analyzing rainfall data in the past 20 years using standard
  precipitation index (SPI) , which is a widely used index in drought analysis. Based
  on SPI6 values for the period October-march, which is the main rainy season in Malawi.
  Each pixel is classified to drought or no drought for each year based on SPI6 values,
  drought year if SPI value for a pixel is less than -1. Next, relative frequency
  is calculated, the number of times drought has occurred in the considered 20 year
  period. This frequency is then converted to probability of drought occurrence in
  a given year. We validated our analysis by comparing NDVI values for the drought
  year against long term average values. Flood layer To identify flood moments in
  Malawi Landsat imagery was studied (1984-2017). Floods were clearly evidenced in
  9 dates. For the clearest and most representative layers the mNDWI (modified Normalized
  Water Index) was calculated. The index mNDWI (McFeeters 1996; Xu 2006) for Landsat
  bands is calculated as follows: (b2GREEN-b7MIRSWIR/b2GREEN+b7MIRSWIR). In this variation
  of the index the higher values are the wettest. A threshold was applied to the mNDWI
  to separate flood from non-flood or water from non-water pixels. The resulting layers
  were aggregated and the final stretched from 0-10, where 0 are the pixels where
  no flood is expected while pixels with 10 are where most frequent flood has been
  evidenced and therefore expected. The largest flood was observed in 2015, as the
  scenes were cloudy the flood extent was manually interpreted from several scenes.
  The evidenced flood dates are: 29 Feb. 1988 low flood, 19 march 1989, 17 march 1997,
  Feb 1998, March 1999 low flood, 2001 since February 16 until end of April, 2007
  17 February since early Feb., 2008 Feb. medium flood, 2015 January - March. The
  water bodies in this layer are not represented and have a value of 0 like the rest
  of land where flood is absent.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/inform-based-prioritization-of-enumeration-areas-in-malawi]'
details: null
exposure:
- asset_type:
    description: Population counts per enumeration area in Southern Malawi
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
    description: Health facilities and secondary schools as accessibility indicators
      per enumeration area
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Enumeration area boundaries from MASDAP were combined with drought
    and flood susceptibility indicators and socioeconomic vulnerability data (poverty,
    accessibility to services) within the INFORM risk framework to generate composite
    hazard, vulnerability, and risk scores for area-level prioritization in the ECHO2
    project across three Traditional Authorities in Southern Malawi.
  sources:
  - id: source_1
    license: null
    name: INFORM Risk Framework
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Malawi Spatial Data Platform (MASDAP)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/inform-based-prioritization-of-enumeration-areas-in-malawi
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposure to drought risk based on INFORM prioritization
      scores
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
        metric: exposure
        modelling: observed
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population exposure to flood risk based on INFORM prioritization
      scores
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
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
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: http://www.masdap.mw/layers/geonode%3Aeas_bnd
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: http://www.inform-index.org/
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: http://www.worldpop.org.uk/data/summary/?doi=10.5258/SOTON/WP00155
- author_names: null
  date_published: null
  doi: null
  id: reference_4
  name: Methodology documentation
  url: http://www.worldpop.org.uk/data/summary/?doi=10.5258/SOTON/WP00157
- author_names: null
  date_published: null
  doi: null
  id: reference_5
  name: Methodology documentation
  url: https://510.global/developing-and-field-testing-a-remoteness-indicator-in-malawi/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CSV with INFORM risk-score per Enumeration Area for whole of Malawi,
    including underlying components and indicators. Can be joined with shapefile on
    EACODE.
  download_url: https://data.humdata.org/dataset/7160a127-d351-40e8-b8ed-244fa9a68a27/resource/798d8c8f-b8b3-482b-97a9-9f45cdcdab47/download/mw_inform_ea.csv
  format: null
  id: resource_798d8c8f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MW_INFORM_EA.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Shapefile on Enumeration Area level (deeper than TA / admin-3). Source:
    NSO (http://www.masdap.mw/layers/geonode%3Aeas_bnd). Join the CSV to this shapefile
    on EACODE, to visualize various attributes.'
  download_url: https://data.humdata.org/dataset/7160a127-d351-40e8-b8ed-244fa9a68a27/resource/4d6bbbea-416e-4347-a628-2fcc7d40f720/download/echo2_prioritization.zip
  format: null
  id: resource_4d6bbbea
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ECHO2_prioritization.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Most up-to-date drought risk indicator (this one should be used instead
    of the one in MW_INFORM_EA.csv). This can also be joined to the shapefile on EACODE.
    This probability (between 0 and 0.25) is later linearly transformed to a 0-10
    score.
  download_url: https://data.humdata.org/dataset/7160a127-d351-40e8-b8ed-244fa9a68a27/resource/c7aff886-d5c1-4e5f-b4fa-35ce02757a88/download/drought_adm4_new.csv
  format: null
  id: resource_c7aff886
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: drought_adm4_new.csv
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-mwi_nlrc510_informbasedprioritization_20170714
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-07-14'
temporal_resolution: null
title: Malawi - INFORM-based prioritization of Enumeration Areas
version: null
vulnerability: null
---

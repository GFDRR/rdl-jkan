---
attributions:
- entity:
    affiliation: null
    email: null
    name: Netherlands Red Cross - 510 Data Initiative
    url: https://data.humdata.org/dataset/bangladesh-floods-august-2017-vulnerability-population-density
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Red Cross Climate Centre
    url: https://data.humdata.org/dataset/bangladesh-floods-august-2017-vulnerability-population-density
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/bangladesh-floods-august-2017-vulnerability-population-density
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/bangladesh-floods-august-2017-vulnerability-population-density
dataset_id: rdls_he-bgd_nlrc510_floodsaugust2017floodingl_20170815
description: 'In this analysis we have combined several data sources around the floods
  in Bangladesh in August 2017. Visualization See attached map for a map visualization
  of this analysis. See http://bit.ly/2uFezkY for a more interactive visualization
  in Carto. Situation Currently, in Bangladesh many water level measuring stations
  measure water levels that are above danger levels. This sets in triggers in motion
  for the partnership of the 510 Data Intitiative and the Red Cross Climate Centre
  to get into action. Indicators and sources In the attached map, we combined several
  sources: Locations of waterlevel stations and their respective excess water levels
  (cms above danger level) at 14/08/2017 (Source: http://www.ffwc.gov.bd/index.php/googlemap?id=20)
  Population density in Bangladesh to quickly see where many people live in comaprison
  to these higher water-level stations. (Source: http://www.worldpop.org.uk/data/summary/?doi=10.5258/SOTON/WP00018
  >> the People per hectare 2015 UN-adjusted totals file is used.) Vulnerability Index:
  we constructed a Vulnerability Index (0-10) based on two sources. First poverty
  incidence was collected from Worldpop (Source: http://www.worldpop.org.uk/data/summary/?doi=10.5258/SOTON/WP00020
  >> The estimated likelihood of living below $2.50/day). Second, we used a Deprivation
  Index which is estimated in the report Lagging District Reports 2015 (Source: http://www.plancomm.gov.bd/wp-content/uploads/2015/02/15_Lagging-Regions-Study.pdf
  > Appendices > Table 20), which combines many socio-economic variables into one
  Deprivation Index through PCA analysis. Detailed methodology Vulnerability The above-mentioned
  poverty source file is on a raster level. This raster level poverty was transformed
  to admin-4 level geographic areas (source: https://data.humdata.org/dataset/bangladesh-admin-level-4-boundaries),
  by taking a population-weighted average. (Source population also Worldpop). The
  district-level PCA components from abovementioned reports were matched to the geodata
  based on district names, and thus joined to the admin-4 level areas, which now contain
  a poverty value as well as Deprivation Index value. Note that all admin-4 areas
  within one district (admin-2) obviously all have the same value. The poverty rates
  do differ between all admin-4 areas. Lastly, both variables were transformed to
  a 0-10 score (linearly), and a geomean was taken to calculate the final index of
  the two. A geomean (as opposed to an arithmetic mean) is often used in calculating
  composite risk indices, for example in the widely used INFORM-framework (www.inform-index.org)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/bangladesh-floods-august-2017-vulnerability-population-density]'
details: null
exposure:
- asset_type:
    description: Population distribution at administrative unit 4 level across Bangladesh
      flood-affected areas
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
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Multiple data sources on the August 2017 Bangladesh floods were integrated,
    including observed water level measurements from monitoring stations across the
    country combined with administrative boundary data and population/vulnerability
    indices at upazila and union levels to assess flood exposure and vulnerability.
  sources:
  - id: source_1
    license: null
    name: Netherlands Red Cross - 510 Data Initiative
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Red Cross Climate Centre
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/bangladesh-floods-august-2017-vulnerability-population-density
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
  url: http://www.ffwc.gov.bd/index.php/googlemap?id=20
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: http://www.worldpop.org.uk/data/summary/?doi=10.5258/SOTON/WP00018
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: http://www.worldpop.org.uk/data/summary/?doi=10.5258/SOTON/WP00020
- author_names: null
  date_published: null
  doi: null
  id: reference_4
  name: Methodology documentation
  url: http://www.plancomm.gov.bd/wp-content/uploads/2015/02/15_Lagging-Regions-Study.pdf
- author_names: null
  date_published: null
  doi: null
  id: reference_5
  name: Methodology documentation
  url: https://data.humdata.org/dataset/bangladesh-admin-level-4-boundaries
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Admin 4 boundaries Bangladesh with Vulnearbility Index (and underlying
    components) attached to it.
  download_url: https://data.humdata.org/dataset/d0e90210-f207-4b96-9b40-dffc506387c4/resource/f8234ae9-5a39-4819-95ef-ef27f2c2daff/download/bangladesh_floods_adm4.zip
  format: null
  id: resource_f8234ae9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bangladesh_floods_adm4.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geolocations of river waterstations in Bangladesh including water levels
    on 14/08/2017 and differences with danger levels.
  download_url: https://data.humdata.org/dataset/d0e90210-f207-4b96-9b40-dffc506387c4/resource/95c71f8a-4755-4662-8fb9-a876bb590cbc/download/geolocations_stations.xlsx
  format: null
  id: resource_95c71f8a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: geolocations_stations.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Map visualization of population density and vulnerability (see methodology
    below).
  download_url: https://data.humdata.org/dataset/d0e90210-f207-4b96-9b40-dffc506387c4/resource/326186f4-609c-4a99-9e29-4166a6fe6070/download/bangladesh_floods_20170817.pdf
  format: null
  id: resource_326186f4
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Bangladesh_floods_20170817.pdf
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_nlrc510_floodsaugust2017floodingl_20170815
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-08-15'
temporal_resolution: null
title: Bangladesh Floods - August 2017 - Flooding levels & Vulnerability
version: null
vulnerability: null
---

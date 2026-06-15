---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/bottom-up-gridded-population-estimates-for-nigeria-version-2-1
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/bottom-up-gridded-population-estimates-for-nigeria-version-2-1
dataset_id: rdls_exp-nga_worldpop_bottomupgriddedpopulation
description: 'This data release provides gridded population estimates (spatial resolution
  of 3 arc-seconds, approximately 100 m grid cells) with national coverage for Nigeria,
  along with estimates of the number of people belonging to various age-gender groups.
  Version 2.1 is an update to the previous version 2.0 gridded population estimates
  and is based on a correction of the settlement map. These model-based population
  estimates most likely represent the time period around 2019, corresponding to the
  period when the satellite imagery was processed to generate building footprints.
  Populations are mapped only into areas where residential settlements are predicted.
  These data were produced by the WorldPop Research Group at the University of Southampton.
  This work was part of the GRID3 Bridge Funding project with funding from the Bill
  and Melinda Gates Foundation (INV-045694). Project partners included the GRID3 Inc
  and the Center for International Earth Science Information Network in the Earth
  Institute at Columbia University. Statistical modelling was originally led by Chris
  Jochem and Doug Leasure with additional support and oversight from Attila Lazar
  and Andy Tatem. Ortis Yankey led the population map update with additional support
  from Edith Darin. The authors followed rigorous procedures designed to ensure that
  the used data, the applied method and thus the results are appropriate and of reasonable
  quality. If users encounter apparent errors or misstatements, they should contact
  WorldPop at release@worldpop.org. SUGGESTED CITATIONS WorldPop. 2023. Bottom-up
  gridded population estimates for Nigeria, version 2.1. WorldPop, University of Southampton.
  DOI: 10.5258/SOTON/WP00765. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/bottom-up-gridded-population-estimates-for-nigeria-version-2-1]'
details: '*SUGGESTED CITATIONS* WorldPop. 2023. Bottom-up gridded population estimates
  for Nigeria, version 2.1. WorldPop, University of Southampton. DOI: 10.5258/SOTON/WP00765'
exposure:
- asset_type:
    description: Gridded population estimates at 100 m resolution with age-gender
      disaggregation for Nigeria circa 2019
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Gridded population estimates derived from satellite-based building
    footprint detection and census data integration, processed to 3 arc-second (approximately
    100 m) grid cells with age-gender stratification. Version 2.1 incorporates corrected
    settlement mapping based on satellite imagery processed circa 2019.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/bottom-up-gridded-population-estimates-for-nigeria-version-2-1
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This README file provides information about the data included in the
    data release, how it was produced, source data that were used, and known assumptions
    and limitations of the results.
  download_url: https://wopr.worldpop.org/download/554
  format: null
  id: resource_6381adc0
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_population_v2_1_README.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 40 geotiff rasters at a spatial resolution of
    3 arc-seconds (approximately 100 m). Each raster provides gridded population estimates
    for an age-gender group per grid cell across Nigeria. We provide 36 rasters for
    the commonly reported age-gender groupings of sequential age classes for males
    and females separately. These are labelled with either an 'm' (male) or an 'f'
    (female) followed by the number of the first year of the age class represented
    by the data. 'f0' and 'm0' are population counts of under 1-year olds for females
    and males, respectively. 'f1' and 'm1' are population counts of 1 to 4 year olds
    for females and males, respectively. Over 4 years old, the age groups are in five
    year bins labelled with a '5', '10', etc. Eighty year olds and over are represented
    by the groups 'f80' and 'm80'. We provide four additional rasters that represent
    demographic groups often targeted by programmes and interventions. These are 'under1'
    (all females and males under the age of 1), 'under5' (all females and males under
    the age of 5), 'under15' (all females and males under the age of 15) and 'f15_49'
    (all females between the ages of 15 and 49, inclusive). These data were produced
    using age-gender proportions from the WorldPop project (WorldPop et al., 2018).
    The age-gender proportions were applied to the gridded population estimates 3(NGA_population_v2_1_gridded.tif)
    to allocate the population to the different age-gender classes. While this data
    represents population counts, values contain decimals, i.e. fractions of people.
    This is because both the input population data and age-gender proportions contain
    decimals. For this reason, it is advised to aggregate the rasters at a coarser
    scale. For example, if four grid cells next to each other have values of 0.25
    this indicates that there is 1 person of that age group somewhere in those four
    grid cells.
  download_url: https://wopr.worldpop.org/download/555
  format: null
  id: resource_02cdd6a7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_population_v2_1_agegender.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 3 arc-seconds (approximately
    100m at the equator), contains estimates of total population size per grid cell
    across Nigeria. NA values represent areas that were mapped as unsettled based
    on a gridded settlement layer derived from building footprints (Maxar Technologies,
    Inc. and Ecopia Tech Corporation, 2021). These data are stored as floating point
    numbers rather than integers to avoid rounding errors in aggregated population
    totals for larger areas.
  download_url: https://wopr.worldpop.org/download/556
  format: null
  id: resource_05247ec4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_population_v2_1_gridded.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nga_worldpop_bottomupgriddedpopulation
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Bottom-up gridded population estimates for Nigeria, version 2.1
version: null
vulnerability: null
---
